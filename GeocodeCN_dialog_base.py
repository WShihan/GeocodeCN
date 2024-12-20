# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GeocodeCN_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GeocodeCNDialogBase(object):
    def setupUi(self, GeocodeCNDialogBase):
        GeocodeCNDialogBase.setObjectName("GeocodeCNDialogBase")
        GeocodeCNDialogBase.setEnabled(True)
        GeocodeCNDialogBase.resize(542, 620)
        GeocodeCNDialogBase.setMinimumSize(QtCore.QSize(250, 550))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(GeocodeCNDialogBase)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(GeocodeCNDialogBase)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setObjectName("tabWidget")
        self.table_batch = QtWidgets.QWidget()
        self.table_batch.setObjectName("table_batch")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.table_batch)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.gbBatch = QtWidgets.QGroupBox(self.table_batch)
        self.gbBatch.setAutoFillBackground(True)
        self.gbBatch.setObjectName("gbBatch")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.gbBatch)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.le_file = QtWidgets.QLineEdit(self.gbBatch)
        self.le_file.setMinimumSize(QtCore.QSize(200, 25))
        self.le_file.setBaseSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(12)
        self.le_file.setFont(font)
        self.le_file.setReadOnly(True)
        self.le_file.setObjectName("le_file")
        self.horizontalLayout_4.addWidget(self.le_file)
        self.btn_file = QtWidgets.QPushButton(self.gbBatch)
        self.btn_file.setMinimumSize(QtCore.QSize(60, 20))
        self.btn_file.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(12)
        self.btn_file.setFont(font)
        self.btn_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_file.setStyleSheet("color: #fff;\n"
"background:#428bca;\n"
"border-radius: 5%;")
        self.btn_file.setObjectName("btn_file")
        self.horizontalLayout_4.addWidget(self.btn_file)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label = QtWidgets.QLabel(self.gbBatch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_12.addWidget(self.label)
        self.cb = QtWidgets.QComboBox(self.gbBatch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb.sizePolicy().hasHeightForWidth())
        self.cb.setSizePolicy(sizePolicy)
        self.cb.setMinimumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(12)
        self.cb.setFont(font)
        self.cb.setObjectName("cb")
        self.horizontalLayout_12.addWidget(self.cb)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lbl_encoding = QtWidgets.QLabel(self.gbBatch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_encoding.sizePolicy().hasHeightForWidth())
        self.lbl_encoding.setSizePolicy(sizePolicy)
        self.lbl_encoding.setMinimumSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(10)
        self.lbl_encoding.setFont(font)
        self.lbl_encoding.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_encoding.setObjectName("lbl_encoding")
        self.horizontalLayout_10.addWidget(self.lbl_encoding)
        self.cb_encoding = QtWidgets.QComboBox(self.gbBatch)
        self.cb_encoding.setMinimumSize(QtCore.QSize(80, 25))
        self.cb_encoding.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(12)
        self.cb_encoding.setFont(font)
        self.cb_encoding.setCurrentText("")
        self.cb_encoding.setObjectName("cb_encoding")
        self.horizontalLayout_10.addWidget(self.cb_encoding)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.btn_start = QtWidgets.QPushButton(self.gbBatch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMinimumSize(QtCore.QSize(0, 20))
        self.btn_start.setMouseTracking(True)
        self.btn_start.setStyleSheet("color: #fff;\n"
"background:#428bca;\n"
"border-radius: 5%;")
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout_7.addWidget(self.btn_start)
        self.verticalLayout_12.addWidget(self.gbBatch)
        self.groupBox = QtWidgets.QGroupBox(self.table_batch)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.leAddress = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leAddress.sizePolicy().hasHeightForWidth())
        self.leAddress.setSizePolicy(sizePolicy)
        self.leAddress.setMinimumSize(QtCore.QSize(0, 25))
        self.leAddress.setMaximumSize(QtCore.QSize(800, 40))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(12)
        self.leAddress.setFont(font)
        self.leAddress.setObjectName("leAddress")
        self.horizontalLayout_5.addWidget(self.leAddress)
        self.btnSingle = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSingle.sizePolicy().hasHeightForWidth())
        self.btnSingle.setSizePolicy(sizePolicy)
        self.btnSingle.setMinimumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.btnSingle.setFont(font)
        self.btnSingle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSingle.setAutoFillBackground(False)
        self.btnSingle.setStyleSheet("color: #fff;\n"
"background:#428bca;\n"
"border-radius: 5%;")
        self.btnSingle.setObjectName("btnSingle")
        self.horizontalLayout_5.addWidget(self.btnSingle)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_12.addWidget(self.groupBox)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tb_loc = QtWidgets.QTextBrowser(self.table_batch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_loc.sizePolicy().hasHeightForWidth())
        self.tb_loc.setSizePolicy(sizePolicy)
        self.tb_loc.setMinimumSize(QtCore.QSize(0, 40))
        self.tb_loc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tb_loc.setStyleSheet("")
        self.tb_loc.setPlaceholderText("")
        self.tb_loc.setObjectName("tb_loc")
        self.verticalLayout_4.addWidget(self.tb_loc)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_add = QtWidgets.QPushButton(self.table_batch)
        self.btn_add.setMinimumSize(QtCore.QSize(80, 20))
        self.btn_add.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.btn_add.setFont(font)
        self.btn_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add.setStyleSheet("color: #fff;\n"
"background:#428bca;\n"
"border-radius: 5%;")
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_2.addWidget(self.btn_add)
        self.btn_export = QtWidgets.QPushButton(self.table_batch)
        self.btn_export.setMinimumSize(QtCore.QSize(60, 20))
        self.btn_export.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.btn_export.setFont(font)
        self.btn_export.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_export.setMouseTracking(False)
        self.btn_export.setStyleSheet("color: #fff;\n"
"background:#428bca;\n"
"border-radius: 5%;")
        self.btn_export.setObjectName("btn_export")
        self.horizontalLayout_2.addWidget(self.btn_export)
        self.btn_clear = QtWidgets.QPushButton(self.table_batch)
        self.btn_clear.setMinimumSize(QtCore.QSize(80, 20))
        self.btn_clear.setMaximumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.btn_clear.setFont(font)
        self.btn_clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear.setStyleSheet("color: #fff;\n"
"background:#428bca;\n"
"border-radius: 5%;")
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_2.addWidget(self.btn_clear)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pb = QtWidgets.QProgressBar(self.table_batch)
        self.pb.setProperty("value", 0)
        self.pb.setObjectName("pb")
        self.verticalLayout.addWidget(self.pb)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_12.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.table_batch, "")
        self.table_one = QtWidgets.QWidget()
        self.table_one.setObjectName("table_one")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.table_one)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.scrollArea = QtWidgets.QScrollArea(self.table_one)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 455, 522))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setAutoFillBackground(True)
        self.groupBox_6.setStyleSheet("color:#428bca")
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lb_service = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_service.setFont(font)
        self.lb_service.setObjectName("lb_service")
        self.horizontalLayout_9.addWidget(self.lb_service)
        self.cb_service = QtWidgets.QComboBox(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_service.sizePolicy().hasHeightForWidth())
        self.cb_service.setSizePolicy(sizePolicy)
        self.cb_service.setMinimumSize(QtCore.QSize(0, 20))
        self.cb_service.setMaximumSize(QtCore.QSize(16777215, 30))
        self.cb_service.setCurrentText("")
        self.cb_service.setObjectName("cb_service")
        self.horizontalLayout_9.addWidget(self.cb_service)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lb_cocurrent = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_cocurrent.setFont(font)
        self.lb_cocurrent.setObjectName("lb_cocurrent")
        self.horizontalLayout_15.addWidget(self.lb_cocurrent)
        self.sp_cocurrent = QtWidgets.QSpinBox(self.groupBox_6)
        self.sp_cocurrent.setMinimum(1)
        self.sp_cocurrent.setMaximum(10)
        self.sp_cocurrent.setProperty("value", 3)
        self.sp_cocurrent.setObjectName("sp_cocurrent")
        self.horizontalLayout_15.addWidget(self.sp_cocurrent)
        self.verticalLayout_11.addLayout(self.horizontalLayout_15)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.cb_crs = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_crs.sizePolicy().hasHeightForWidth())
        self.cb_crs.setSizePolicy(sizePolicy)
        self.cb_crs.setMinimumSize(QtCore.QSize(0, 20))
        self.cb_crs.setMaximumSize(QtCore.QSize(16777215, 30))
        self.cb_crs.setObjectName("cb_crs")
        self.cb_crs.addItem("")
        self.cb_crs.addItem("")
        self.cb_crs.addItem("")
        self.horizontalLayout_7.addWidget(self.cb_crs)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.le_key_baidu = QtWidgets.QLineEdit(self.groupBox_2)
        self.le_key_baidu.setMinimumSize(QtCore.QSize(0, 25))
        self.le_key_baidu.setObjectName("le_key_baidu")
        self.horizontalLayout_6.addWidget(self.le_key_baidu)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.le_key_gaode = QtWidgets.QLineEdit(self.groupBox_5)
        self.le_key_gaode.setMinimumSize(QtCore.QSize(0, 25))
        self.le_key_gaode.setText("")
        self.le_key_gaode.setObjectName("le_key_gaode")
        self.horizontalLayout_8.addWidget(self.le_key_gaode)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.gb_OSM = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.gb_OSM.setObjectName("gb_OSM")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.gb_OSM)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.gb_OSM)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.le_key_mapbox = QtWidgets.QLineEdit(self.gb_OSM)
        self.le_key_mapbox.setMinimumSize(QtCore.QSize(0, 25))
        self.le_key_mapbox.setObjectName("le_key_mapbox")
        self.horizontalLayout.addWidget(self.le_key_mapbox)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.gb_OSM)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        self.le_proxy_osm = QtWidgets.QLineEdit(self.groupBox_3)
        self.le_proxy_osm.setMinimumSize(QtCore.QSize(0, 25))
        self.le_proxy_osm.setObjectName("le_proxy_osm")
        self.horizontalLayout_11.addWidget(self.le_proxy_osm)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_13.addWidget(self.label_5)
        self.le_key_here = QtWidgets.QLineEdit(self.groupBox_4)
        self.le_key_here.setMinimumSize(QtCore.QSize(0, 25))
        self.le_key_here.setObjectName("le_key_here")
        self.horizontalLayout_13.addWidget(self.le_key_here)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_10.addWidget(self.scrollArea)
        self.btn_apply = QtWidgets.QPushButton(self.table_one)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_apply.sizePolicy().hasHeightForWidth())
        self.btn_apply.setSizePolicy(sizePolicy)
        self.btn_apply.setMinimumSize(QtCore.QSize(0, 20))
        self.btn_apply.setStyleSheet("color: #fff;\n"
"background:#428bca;\n"
"border-radius: 5%;")
        self.btn_apply.setObjectName("btn_apply")
        self.verticalLayout_10.addWidget(self.btn_apply)
        self.tabWidget.addTab(self.table_one, "")
        self.verticalLayout_2.addWidget(self.tabWidget)

        self.retranslateUi(GeocodeCNDialogBase)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(GeocodeCNDialogBase)

    def retranslateUi(self, GeocodeCNDialogBase):
        _translate = QtCore.QCoreApplication.translate
        GeocodeCNDialogBase.setWindowTitle(_translate("GeocodeCNDialogBase", "GeocodeCN"))
        self.gbBatch.setTitle(_translate("GeocodeCNDialogBase", "批量"))
        self.le_file.setPlaceholderText(_translate("GeocodeCNDialogBase", "选择csv文件"))
        self.btn_file.setToolTip(_translate("GeocodeCNDialogBase", "选择csv文件"))
        self.btn_file.setText(_translate("GeocodeCNDialogBase", "文件"))
        self.label.setToolTip(_translate("GeocodeCNDialogBase", "用作地理编码的列"))
        self.label.setText(_translate("GeocodeCNDialogBase", "地址列"))
        self.lbl_encoding.setToolTip(_translate("GeocodeCNDialogBase", "用作地理编码的列"))
        self.lbl_encoding.setText(_translate("GeocodeCNDialogBase", "编码"))
        self.btn_start.setText(_translate("GeocodeCNDialogBase", "开始"))
        self.groupBox.setTitle(_translate("GeocodeCNDialogBase", "单个"))
        self.leAddress.setPlaceholderText(_translate("GeocodeCNDialogBase", "在此输入地址名称，尽量详细"))
        self.btnSingle.setToolTip(_translate("GeocodeCNDialogBase", "获取该地址坐标"))
        self.btnSingle.setText(_translate("GeocodeCNDialogBase", "开始"))
        self.btn_add.setToolTip(_translate("GeocodeCNDialogBase", "生成图层"))
        self.btn_add.setText(_translate("GeocodeCNDialogBase", "添加到地图"))
        self.btn_export.setToolTip(_translate("GeocodeCNDialogBase", "导出为csv文件"))
        self.btn_export.setText(_translate("GeocodeCNDialogBase", "导出为"))
        self.btn_clear.setToolTip(_translate("GeocodeCNDialogBase", "清除当前编码数据"))
        self.btn_clear.setText(_translate("GeocodeCNDialogBase", "清除"))
        self.pb.setToolTip(_translate("GeocodeCNDialogBase", "编码进度"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.table_batch), _translate("GeocodeCNDialogBase", "编码"))
        self.groupBox_6.setTitle(_translate("GeocodeCNDialogBase", "当前使用"))
        self.lb_service.setText(_translate("GeocodeCNDialogBase", "地图服务"))
        self.lb_cocurrent.setText(_translate("GeocodeCNDialogBase", "并发数量"))
        self.groupBox_2.setTitle(_translate("GeocodeCNDialogBase", "百度地图"))
        self.label_6.setText(_translate("GeocodeCNDialogBase", "坐标系"))
        self.cb_crs.setItemText(0, _translate("GeocodeCNDialogBase", "WGS84"))
        self.cb_crs.setItemText(1, _translate("GeocodeCNDialogBase", "百度坐标系"))
        self.cb_crs.setItemText(2, _translate("GeocodeCNDialogBase", "国测局坐标系"))
        self.label_3.setText(_translate("GeocodeCNDialogBase", "密   钥"))
        self.le_key_baidu.setPlaceholderText(_translate("GeocodeCNDialogBase", "百度地图平台密钥"))
        self.groupBox_5.setTitle(_translate("GeocodeCNDialogBase", "高德地图"))
        self.label_8.setText(_translate("GeocodeCNDialogBase", "密   钥"))
        self.le_key_gaode.setPlaceholderText(_translate("GeocodeCNDialogBase", "高德地图密钥"))
        self.gb_OSM.setTitle(_translate("GeocodeCNDialogBase", "Mapbox"))
        self.label_2.setText(_translate("GeocodeCNDialogBase", "密   钥"))
        self.le_key_mapbox.setPlaceholderText(_translate("GeocodeCNDialogBase", "Mapbox平台密钥"))
        self.groupBox_3.setTitle(_translate("GeocodeCNDialogBase", "OSM"))
        self.label_4.setText(_translate("GeocodeCNDialogBase", "地    址"))
        self.le_proxy_osm.setToolTip(_translate("GeocodeCNDialogBase", "可指定代理地址"))
        self.le_proxy_osm.setPlaceholderText(_translate("GeocodeCNDialogBase", "OSM 地理编码转发地址，默认官方地址"))
        self.groupBox_4.setTitle(_translate("GeocodeCNDialogBase", "Here"))
        self.label_5.setText(_translate("GeocodeCNDialogBase", "密   钥"))
        self.le_key_here.setPlaceholderText(_translate("GeocodeCNDialogBase", "Here平台密钥"))
        self.btn_apply.setText(_translate("GeocodeCNDialogBase", "应用"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.table_one), _translate("GeocodeCNDialogBase", "配置"))
