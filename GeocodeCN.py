# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeocodeCN
                                 A QGIS plugin
 crs getter
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-01-03
        git sha              : $Format:%H$
        copyright            : (C) 2022 by ShihanW
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
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsPointXY, QgsProject
from qgis.PyQt.QtWidgets import QFileDialog, QAction, QMessageBox
import pandas as pd
from .gcs import Baidu, Crs_gen
# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .GeocodeCN_dialog import GeocodeCNDialog
import os.path


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
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'GeocodeCN_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&GeocodeCN')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None
        self.locs = []
        self.file_selected = False

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
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

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
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/GeocodeCN/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u''),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&GeocodeCN'),
                action)
            self.iface.removeToolBarIcon(action)


    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = GeocodeCNDialog()
            self.dlg.btn_file.clicked.connect(self.select_csv)
            self.dlg.btn_start.clicked.connect(self.start)
            self.dlg.btn_export.clicked.connect(self.export)
            self.dlg.btn_add.clicked.connect(self.add_lyr)
            self.dlg.btn_clear.clicked.connect(self.clear)

        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass

    def select_csv(self):
        # 先清除原文字
        self.clear()
        try:
            file_name, _filter = QFileDialog.getOpenFileName(self.dlg, "选择文件", r"E:\Desktop\GisFile\sheet_text_asset", "*.csv")
            if file_name:
                self.file_selected = True
                self.dlg.le_file.setText(file_name)
                df = pd.read_csv(file_name, encoding="gbk")
                self.dlg.pb.setMaximum(df.count()[0])
                del df
                self.reader = csv.DictReader(open(self.dlg.le_file.text(), 'r', encoding="gbk"))
                self.fields = self.reader.fieldnames
                self.dlg.cb.addItems(self.fields)
            else:
                raise FileNotFoundError("未选择文件！")
        except Exception as e:
            QMessageBox.information(self.dlg, "状态", str(e), QMessageBox.Yes)
    def start(self):
        """
        编码
        """
        try:
            if self.file_selected:
                col_sele = self.dlg.cb.currentText()
                self.th = Crs_gen(self.reader, col_sele)
                self.th.signal.connect(self.collect_and_print)
                self.th.finished.connect(lambda :self.dlg.pb.setValue(0))
                self.th.start()
            else:
                raise FileNotFoundError("未选择文件！")
        except Exception as e:
            QMessageBox.critical(self.dlg , '状态' , str(e) , QMessageBox.Ok)

    def collect_and_print(self, location):
        value = self.dlg.pb.value()
        self.dlg.pb.setValue(value + 1)
        if len(location) != 0:
            loc = location[-1]
            address = location[0]
            attr = location[1]
            self.locs.append(attr + loc)
            self.dlg.tb_loc.append("地址：{}\t经度：{}\t纬度：{}".format(address, loc[0], loc[1]))
            # self.dlg.tb_loc.setText(str(len(self.locs)))
        else:
            pass



    def export(self):
        try:
            if len(self.locs) != 0:
                output_file, _filter = QFileDialog.getSaveFileName(self.dlg, "另存为csv", "", "*.csv")
                if output_file:
                    writer = csv.writer(open(output_file, 'a', encoding="gbk", newline=""))
                    writer.writerow(self.fields + ['lon', 'lat'])
                    for r in self.locs:
                        writer.writerow(r)
                    QMessageBox.information(self.dlg, '状态', '保存成功！', QMessageBox.Yes)
                    self.dlg.setWindowTitle("GeocodeCN-已保存")
                else:
                    pass
            else:
                raise FileNotFoundError("未开始编码！")
        except Exception as e:
            QMessageBox.critical(self.dlg, '状态',str(e), QMessageBox.Yes)


    def add_lyr(self):
        try:
            if len(self.locs) != 0:
                lyr = QgsVectorLayer("Point", "geocode_temp_lyr", "memory")
                pr = lyr.dataProvider()
                attr = [QgsField(i, QVariant.String) for i in self.fields + ['lon', 'lat']]
                pr.addAttributes(attr)
                lyr.updateFields()
                for r in self.locs:
                    y = r[-1]
                    x = r[-2]
                    f = QgsFeature()
                    f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(x, y)))
                    f.setAttributes(r)
                    pr.addFeature(f)
                lyr.updateExtents()
                QgsProject.instance().addMapLayer(lyr)
                QMessageBox.information(self.dlg, "状态", "添加图层成功！", QMessageBox.Yes)
            else:
                raise ValueError("无编码数据！")

        except Exception as e:
            QMessageBox.critical(self.dlg, '状态', str(e), QMessageBox.Yes)

    def clear(self):
        self.dlg.le_file.setText("")
        self.dlg.tb_loc.setText("")
        self.file_selected = False
        self.dlg.setWindowTitle("GeocodeCN")
        self.locs.clear()
        self.dlg.cb.clear()
        self.locs.clear()
