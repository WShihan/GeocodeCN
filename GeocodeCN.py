# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeocodeCN
                                 address --> coordinates
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-01-03
        git sha              : $Format:%H$
        copyright            : (C) 2022 by WangShihan
        email                : 3443327820@qq.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import csv
import encodings
import os
import chardet
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtCore import QVariant
from qgis.core import (
    QgsVectorLayer,
    QgsField,
    QgsFeature,
    QgsGeometry,
    QgsPointXY,
    QgsProject,
    Qgis,
)
from qgis.PyQt.QtWidgets import QFileDialog, QAction, QMessageBox
from .gcs import Baidu, CrsGen, Nominatim, Here, Mapbox, Geocoder
from .utils import CrsTypeEnum
from .config import Config

# Initialize Qt resources from file resources.py
from .resources import *

# Import the code for the dialog
from .GeocodeCN_dialog import GeocodeCNDialog


class GeocodeCN:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.th = None
        self.iface = iface
        self.dlg = GeocodeCNDialog()
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir, 'i18n', 'GeocodeCN_{}.qm'.format(locale)
        )

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.settings = QSettings()
        self.menu = self.tr(u'&GeocodeCN')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None
        self.locs = []
        self.fields = []
        self.file_selected = False
        self.crsMap = {
            "百度坐标系": CrsTypeEnum.bd,
            "WGS84": CrsTypeEnum.bd2wgs,
            "国测局坐标系": CrsTypeEnum.bd2gcj,
        }
        self.running: bool = False
        self.delimiter: str = ''
        self.encoding: str = ''
        self.address_list = []
        self.config = Config()
        self.read_config()

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('GeocodeCN', message)

    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None,
    ):
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        icon_path = ':/plugins/GeocodeCN/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u''),
            callback=self.run,
            parent=self.iface.mainWindow(),
        )
        # will be set False in run()
        self.first_start = True
        if self.first_start:
            self.first_start = False
            # 绑定信号
            self.dlg.btn_file.clicked.connect(self.on_csv_select)
            self.dlg.btn_start.clicked.connect(self.on_geocode_bach)
            self.dlg.btn_export.clicked.connect(self.on_csv_export)
            self.dlg.btn_add.clicked.connect(self.on_add_lyr)
            self.dlg.btn_clear.clicked.connect(self.on_clear)
            self.dlg.btnSingle.clicked.connect(self.on_single_geocode)
            self.dlg.btn_apply.clicked.connect(self.on_config_apply)
            self.dlg.showEvent = self.window_show_eventHandler  # type: ignore

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(self.tr(u'&GeocodeCN'), action)
            self.iface.removeToolBarIcon(action)

    def window_show_eventHandler(self, evt):
        pass
        # self.read_config()

    def run(self):
        self.dlg.show()
        self.dlg.exec_()

    def on_geocode_bach(self):
        """Run method that performs all the real work"""
        if self.running:
            QMessageBox.information(self.dlg, '状态', '正在匹配中……', QMessageBox.Yes)
            return
        try:
            if self.file_selected and len(self.locs) == 0:
                col_sel = self.dlg.cb.currentText()
                handler = self.detect_geocoder()
                self.th = CrsGen(self.address_list, col_sel, handler)
                # 单次匹配完成回调
                self.th.row_signal.connect(self.collect_and_print)
                # 所有匹配完成回调
                self.th.finish_signal.connect(self.geocoding_finished)
                # self.th.finished.connect(lambda: self.dlg.pb.setValue(0))
                self.set_tip(self.tr("正在匹配中..."), Qgis.Success)  # type: ignore
                # 进度条启动提醒开始匹配中
                self.dlg.pb.setValue(1)
                self.running = True
                self.th.start()
            else:
                raise FileNotFoundError("请选择匹配文件或清除当前数据！")
        except Exception as e:
            QMessageBox.critical(self.dlg, '状态', str(e), QMessageBox.Ok)

    def on_csv_select(self):
        """
        选择文件
        """
        try:
            file_name, _filter = QFileDialog.getOpenFileName(
                self.dlg, "选择文件", r"E:\Desktop\GisFile\sheet_text_asset", "*.csv"
            )
            # 是否选择文件
            if file_name:
                self.file_selected = True
                self.dlg.le_file.setText(file_name)
                csv_path = self.dlg.le_file.text()
                self.encoding = self.dlg.cb_encoding.currentText()
                csv_detect = self.csv_detect(csv_path, self.encoding)
                if len(csv_detect) == 0:
                    raise Exception("解析CSV错误！")
                else:
                    self.delimiter = csv_detect[0]
                    self.fields.clear()
                    self.fields += csv_detect[1]  # type: ignore
                    self.address_list.clear()
                    self.address_list = list(csv_detect[2])
                    self.dlg.cb.addItems(self.fields)
                    self.dlg.pb.setMaximum(len(self.address_list))
            else:
                pass
        except Exception as e:
            QMessageBox.information(self.dlg, "状态", str(e), QMessageBox.Yes)

    def on_single_geocode(self):
        """
        单一匹配地址
        """
        try:
            self.clear()
            self.dlg.pb.setMaximum(10)
            self.dlg.pb.setValue(3)
            handler = self.detect_geocoder()
            address = self.dlg.leAddress.text()
            self.fields: list = ['地址']
            res = handler.search(address)
            if len(res) > 0:
                if res[0] == 1:
                    loc = res[1]
                    self.locs.clear()
                    self.locs.append([address] + loc)
                    self.dlg.tb_loc.append(
                        "地址：{:<100}\n经度：{:<50}\t纬度：{:<50} \n{:-<58}".format(
                            address, loc[0], loc[1], ""
                        )
                    )
                self.dlg.pb.setValue(10)
                self.set_tip(self.tr("匹配完成！"), Qgis.Success)  # type: ignore
            else:
                self.dlg.pb.setValue(10)
                raise Exception("无地址数据！")
        except Exception as e:
            QMessageBox.information(self.dlg, '状态', str(e), QMessageBox.Ok)

    def collect_and_print(self, result):
        """
        自定义信号槽，接收子线程坐标信号
        """
        value = self.dlg.pb.value()
        self.dlg.pb.setValue(value + 1)
        if len(result) > 1 and result[-1] == '':
            address = result[0]
            attr = result[1]
            loc = result[2]
            print(result)
            self.locs.append(attr + loc)
            self.dlg.tb_loc.append(
                "地址：{:<50}\n经度：{:<20}\t纬度：{:<20} \n{:-<100}".format(
                    address, loc[0], loc[1], ""
                )
            )
        else:
            self.dlg.tb_loc.append(
                "地址：{:<50}未获取到坐标 \t 原因：{:<50} \n{:#<50}".format(
                    result[0], result[-1], ""
                )
            )

    def geocoding_finished(self, res):
        self.running = False
        self.set_tip(self.tr("匹配完成！"), Qgis.Success)  # type: ignore

    def on_csv_export(self):
        """
        导出为csv文件
        """
        try:
            # 是否存在已编码数据
            if len(self.locs) != 0:
                output_file, _filter = QFileDialog.getSaveFileName(
                    self.dlg, "另存为csv", "", "*.csv"
                )
                if output_file:
                    writer = csv.writer(
                        open(output_file, 'a', encoding="gbk", newline=""),
                        delimiter=self.delimiter,
                    )
                    writer.writerow(self.fields + ['lon', 'lat'])
                    for r in self.locs:
                        writer.writerow(r)
                    # 提醒并修改窗口标题
                    self.set_tip(self.tr("成功导出为csv！"), Qgis.Success)  # type: ignore
                    # QMessageBox.information(self.dlg, '状态', '保存成功！', QMessageBox.Yes)
                    self.dlg.setWindowTitle("GeocodeCN-已保存")
                else:
                    raise Exception("保存出错!")
            else:
                raise FileNotFoundError("无坐标数据！")
        except Exception as e:
            QMessageBox.critical(self.dlg, '状态', str(e), QMessageBox.Yes)

    def on_add_lyr(self):
        """
        添加临时图层至地图窗口
        """
        try:
            # 是否含有编码数据
            if len(self.locs) != 0:
                # 创建临时图层
                lyr = QgsVectorLayer("Point", "geocode_temp_lyr", "memory")
                # 添加属性字段
                pr = lyr.dataProvider()
                attr = [
                    QgsField(i, QVariant.String) for i in self.fields + ['lon', 'lat']
                ]

                pr.addAttributes(attr)
                lyr.updateFields()
                for r in self.locs:
                    y = r[-1]
                    x = r[-2]
                    # 创建要素
                    f = QgsFeature()
                    # 设置要素几何
                    f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(x, y)))
                    # 添加字段数据
                    f.setAttributes(r)
                    pr.addFeature(f)
                lyr.updateExtents()
                # 添加至地图
                QgsProject.instance().addMapLayer(lyr)
                self.set_tip(self.tr("成功添加图层！"), Qgis.Success)  # type: ignore
            else:
                raise ValueError("无坐标数据！")
        except Exception as e:
            QMessageBox.critical(self.dlg, '状态', str(e), QMessageBox.Yes)

    def on_clear(self):
        """
        清除窗口信息
        """
        try:
            self.clear()
            self.set_tip(self.tr("清除成功"), Qgis.Success)  # type: ignore
        except Exception as e:
            self.set_tip(self.tr("清除成功"), Qgis.Failed)  # type: ignore

    def set_tip(self, tip: str, isSuccess: bool):
        if isSuccess:
            responseType = Qgis.Success
        else:
            responseType = Qgis.Warning
        self.iface.messageBar().pushMessage(self.tr(tip), responseType)

    def clear(self):
        self.dlg.le_file.setText("")
        # self.dlg.leAddress.setText("")
        self.dlg.tb_loc.setText("")
        self.file_selected = False
        self.dlg.setWindowTitle("GeocodeCN")
        self.locs.clear()
        self.fields.clear()
        self.dlg.cb.clear()
        self.dlg.pb.setValue(0)

    def detect_geocoder(self) -> Geocoder:

        service = self.config.active_service
        if service == '百度地图':
            if self.config.baidu_key == '':
                raise FileNotFoundError("请先在配置中填写百度地图的key！")
            crs = self.crsMap[self.dlg.cb_crs.currentText()]
            return Baidu(self.config.baidu_key, transform=crs)
        elif service == 'Here':
            if self.config.here_key == '':
                raise FileNotFoundError("请先在配置中填写Here的key！")
            return Here(self.config.here_key)
        elif service == 'Mapbox':
            if self.config.mapbox_key == '':
                raise FileNotFoundError("请先在配置中填写Mapbox的key！")
            return Mapbox(self.config.mapbox_key)
        else:
            if self.config.osm_proxy:
                return Nominatim(proxy=self.config.osm_proxy)
            else:
                return Nominatim()

    def csv_detect(self, file_path: str, encoding: str = 'utf-8') -> tuple:
        # 定义常见的分隔符
        delimiters = [',', ';', '\t', '|', ':']
        for sep in delimiters:
            with open(file_path, 'r', encoding=encoding) as f:
                reader = csv.DictReader(f, delimiter=sep)
                fields = reader.fieldnames
                if fields is not None:
                    if len(fields) == 1:
                        continue
                    else:
                        return (sep, fields, list(reader))
                else:
                    continue
        return tuple()

    def read_config(self):
        self.address_list = []
        self.config.baidu_crs = self.settings.value('BAIDU_CRS')
        self.config.active_service = self.settings.value('ACTIVE_SERVICE')
        self.config.baidu_key = self.settings.value('BAIDU_KEY')
        self.config.here_key = self.settings.value('HERE_KEY')
        self.config.mapbox_key = self.settings.value('MAPBOX_KEY')
        self.config.osm_proxy = self.settings.value('OSM_PROXY')

        self.dlg.cb_encoding.addItems(sorted(encodings.aliases.aliases.keys()))
        self.dlg.cb_encoding.setCurrentText('utf8')
        self.dlg.cb_service.setCurrentText(self.config.active_service)
        self.dlg.cb_crs.setCurrentText(self.config.baidu_crs)
        self.dlg.le_key_baidu.setText(self.config.baidu_key)
        self.dlg.le_key_here.setText(self.config.here_key)
        self.dlg.le_key_mapbox.setText(self.config.mapbox_key)
        self.dlg.le_proxy_osm.setText(self.config.osm_proxy)

    def on_config_apply(self):
        self.settings.setValue('BAIDU_CRS', self.dlg.cb_crs.currentText())
        self.settings.setValue('BAIDU_KEY', self.dlg.le_key_baidu.text())
        self.settings.setValue('MAPBOX_KEY', self.dlg.le_key_mapbox.text())
        self.settings.setValue('HERE_KEY', self.dlg.le_key_here.text())
        self.settings.setValue('OSM_PROXY', self.dlg.le_proxy_osm.text())
        self.settings.setValue('ACTIVE_SERVICE', self.dlg.cb_service.currentText())
        self.set_tip(self.tr("配置已保存"), Qgis.Success)  # type: ignore

        # 热更新配置
        self.read_config()
