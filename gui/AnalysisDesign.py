# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnalysisDesign.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 1002)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Layout = QtWidgets.QGridLayout(self.centralwidget)
        self.Layout.setObjectName("Layout")
        self.TCSPCgroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.TCSPCgroupBox.setMinimumSize(QtCore.QSize(0, 540))
        self.TCSPCgroupBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.TCSPCgroupBox.setObjectName("TCSPCgroupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.TCSPCgroupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 50, 791, 431))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.tcspcLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.tcspcLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.tcspcLayout.setContentsMargins(0, 0, 0, 0)
        self.tcspcLayout.setObjectName("tcspcLayout")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.TCSPCgroupBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 140, 161, 99))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_NP = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_NP.setChecked(True)
        self.radioButton_NP.setObjectName("radioButton_NP")
        self.buttonGroup_tcspcmode = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_tcspcmode.setObjectName("buttonGroup_tcspcmode")
        self.buttonGroup_tcspcmode.addButton(self.radioButton_NP)
        self.verticalLayout_2.addWidget(self.radioButton_NP)
        self.radioButton_origami_manual = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_origami_manual.setObjectName("radioButton_origami_manual")
        self.buttonGroup_tcspcmode.addButton(self.radioButton_origami_manual)
        self.verticalLayout_2.addWidget(self.radioButton_origami_manual)
        self.radioButton_origami_auto = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_origami_auto.setObjectName("radioButton_origami_auto")
        self.buttonGroup_tcspcmode.addButton(self.radioButton_origami_auto)
        self.verticalLayout_2.addWidget(self.radioButton_origami_auto)
        self.checkBox_TraceSelection = QtWidgets.QCheckBox(self.TCSPCgroupBox)
        self.checkBox_TraceSelection.setGeometry(QtCore.QRect(20, 260, 149, 23))
        self.checkBox_TraceSelection.setChecked(False)
        self.checkBox_TraceSelection.setObjectName("checkBox_TraceSelection")
        self.pushButton_addWindow = QtWidgets.QPushButton(self.TCSPCgroupBox)
        self.pushButton_addWindow.setEnabled(False)
        self.pushButton_addWindow.setGeometry(QtCore.QRect(20, 290, 141, 34))
        self.pushButton_addWindow.setObjectName("pushButton_addWindow")
        self.pushButton_saveOntimes = QtWidgets.QPushButton(self.TCSPCgroupBox)
        self.pushButton_saveOntimes.setEnabled(False)
        self.pushButton_saveOntimes.setGeometry(QtCore.QRect(20, 370, 141, 34))
        self.pushButton_saveOntimes.setObjectName("pushButton_saveOntimes")
        self.PushButton_LoadOntimes = QtWidgets.QPushButton(self.TCSPCgroupBox)
        self.PushButton_LoadOntimes.setEnabled(False)
        self.PushButton_LoadOntimes.setGeometry(QtCore.QRect(20, 410, 141, 34))
        self.PushButton_LoadOntimes.setObjectName("PushButton_LoadOntimes")
        self.threshold_lineEdit = QtWidgets.QLineEdit(self.TCSPCgroupBox)
        self.threshold_lineEdit.setGeometry(QtCore.QRect(125, 85, 56, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threshold_lineEdit.sizePolicy().hasHeightForWidth())
        self.threshold_lineEdit.setSizePolicy(sizePolicy)
        self.threshold_lineEdit.setFrame(True)
        self.threshold_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.threshold_lineEdit.setObjectName("threshold_lineEdit")
        self.threshold_label = QtWidgets.QLabel(self.TCSPCgroupBox)
        self.threshold_label.setGeometry(QtCore.QRect(20, 80, 101, 31))
        self.threshold_label.setObjectName("threshold_label")
        self.binWidthlineEdit = QtWidgets.QLineEdit(self.TCSPCgroupBox)
        self.binWidthlineEdit.setEnabled(True)
        self.binWidthlineEdit.setGeometry(QtCore.QRect(125, 55, 56, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.binWidthlineEdit.sizePolicy().hasHeightForWidth())
        self.binWidthlineEdit.setSizePolicy(sizePolicy)
        self.binWidthlineEdit.setMaximumSize(QtCore.QSize(1000, 1000))
        self.binWidthlineEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.binWidthlineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.binWidthlineEdit.setMaxLength(1000)
        self.binWidthlineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.binWidthlineEdit.setObjectName("binWidthlineEdit")
        self.binWidthlabel = QtWidgets.QLabel(self.TCSPCgroupBox)
        self.binWidthlabel.setGeometry(QtCore.QRect(20, 50, 101, 31))
        self.binWidthlabel.setScaledContents(False)
        self.binWidthlabel.setObjectName("binWidthlabel")
        self.Layout.addWidget(self.TCSPCgroupBox, 1, 0, 1, 1)
        self.PSFgroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.PSFgroupBox.setMinimumSize(QtCore.QSize(1000, 0))
        self.PSFgroupBox.setObjectName("PSFgroupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.PSFgroupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(570, 20, 401, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.psfLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.psfLayout.setContentsMargins(0, 0, 0, 0)
        self.psfLayout.setObjectName("psfLayout")
        self.psfScrollbar = QtWidgets.QScrollBar(self.PSFgroupBox)
        self.psfScrollbar.setEnabled(False)
        self.psfScrollbar.setGeometry(QtCore.QRect(570, 400, 401, 16))
        self.psfScrollbar.setMaximum(19)
        self.psfScrollbar.setPageStep(1)
        self.psfScrollbar.setOrientation(QtCore.Qt.Horizontal)
        self.psfScrollbar.setObjectName("psfScrollbar")
        self.PSFfile_groupBox = QtWidgets.QGroupBox(self.PSFgroupBox)
        self.PSFfile_groupBox.setGeometry(QtCore.QRect(10, 30, 541, 221))
        self.PSFfile_groupBox.setObjectName("PSFfile_groupBox")
        self.psfFileEditBox = QtWidgets.QLineEdit(self.PSFfile_groupBox)
        self.psfFileEditBox.setGeometry(QtCore.QRect(20, 40, 489, 25))
        self.psfFileEditBox.setObjectName("psfFileEditBox")
        self.browseFilePSF = QtWidgets.QPushButton(self.PSFfile_groupBox)
        self.browseFilePSF.setGeometry(QtCore.QRect(20, 70, 161, 31))
        self.browseFilePSF.setObjectName("browseFilePSF")
        self.PSFmode_groupBox = QtWidgets.QGroupBox(self.PSFfile_groupBox)
        self.PSFmode_groupBox.setGeometry(QtCore.QRect(60, 120, 201, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PSFmode_groupBox.sizePolicy().hasHeightForWidth())
        self.PSFmode_groupBox.setSizePolicy(sizePolicy)
        self.PSFmode_groupBox.setObjectName("PSFmode_groupBox")
        self.radioButton_exppsf = QtWidgets.QRadioButton(self.PSFmode_groupBox)
        self.radioButton_exppsf.setGeometry(QtCore.QRect(20, 60, 161, 20))
        self.radioButton_exppsf.setObjectName("radioButton_exppsf")
        self.radioButton_psffit = QtWidgets.QRadioButton(self.PSFmode_groupBox)
        self.radioButton_psffit.setGeometry(QtCore.QRect(20, 30, 101, 23))
        self.radioButton_psffit.setChecked(True)
        self.radioButton_psffit.setObjectName("radioButton_psffit")
        self.layoutWidget = QtWidgets.QWidget(self.PSFfile_groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(320, 131, 181, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.LoadPSFButton = QtWidgets.QPushButton(self.layoutWidget)
        self.LoadPSFButton.setObjectName("LoadPSFButton")
        self.verticalLayout_5.addWidget(self.LoadPSFButton)
        self.pushButton_saveFit = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_saveFit.setObjectName("pushButton_saveFit")
        self.verticalLayout_5.addWidget(self.pushButton_saveFit)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.TCSPCfile_groupBox = QtWidgets.QGroupBox(self.PSFgroupBox)
        self.TCSPCfile_groupBox.setGeometry(QtCore.QRect(10, 260, 541, 131))
        self.TCSPCfile_groupBox.setObjectName("TCSPCfile_groupBox")
        self.tcspcEditBox = QtWidgets.QLineEdit(self.TCSPCfile_groupBox)
        self.tcspcEditBox.setEnabled(True)
        self.tcspcEditBox.setGeometry(QtCore.QRect(30, 40, 489, 25))
        self.tcspcEditBox.setMouseTracking(False)
        self.tcspcEditBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tcspcEditBox.setObjectName("tcspcEditBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.TCSPCfile_groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 70, 489, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.browseFileTCSPC = QtWidgets.QPushButton(self.layoutWidget1)
        self.browseFileTCSPC.setToolTipDuration(-1)
        self.browseFileTCSPC.setObjectName("browseFileTCSPC")
        self.horizontalLayout_2.addWidget(self.browseFileTCSPC)
        self.LoadTCSPCButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.LoadTCSPCButton.setObjectName("LoadTCSPCButton")
        self.horizontalLayout_2.addWidget(self.LoadTCSPCButton)
        self.Layout.addWidget(self.PSFgroupBox, 0, 0, 1, 1)
        self.ParametergroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ParametergroupBox.sizePolicy().hasHeightForWidth())
        self.ParametergroupBox.setSizePolicy(sizePolicy)
        self.ParametergroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.ParametergroupBox.setObjectName("ParametergroupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.ParametergroupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 40, 342, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(10, 0, 20, 0)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.label_numPSF = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_numPSF.setObjectName("label_numPSF")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_numPSF)
        self.spinBox_donuts = QtWidgets.QSpinBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_donuts.sizePolicy().hasHeightForWidth())
        self.spinBox_donuts.setSizePolicy(sizePolicy)
        self.spinBox_donuts.setProperty("value", 4)
        self.spinBox_donuts.setDisplayIntegerBase(10)
        self.spinBox_donuts.setObjectName("spinBox_donuts")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_donuts)
        self.label_SBR = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_SBR.setObjectName("label_SBR")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_SBR)
        self.lineEdit_sbr = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_sbr.setEnabled(True)
        self.lineEdit_sbr.setObjectName("lineEdit_sbr")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_sbr)
        self.label_winlen = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_winlen.setObjectName("label_winlen")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_winlen)
        self.lineEdit_winlen = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_winlen.setObjectName("lineEdit_winlen")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_winlen)
        self.label_lifetime_window_i = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_lifetime_window_i.setObjectName("label_lifetime_window_i")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_lifetime_window_i)
        self.lineEdit_lifetimewin_i = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_lifetimewin_i.setObjectName("lineEdit_lifetimewin_i")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_lifetimewin_i)
        self.label_lifetime_window_f = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_lifetime_window_f.setObjectName("label_lifetime_window_f")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_lifetime_window_f)
        self.lineEdit_lifetimewin_f = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_lifetimewin_f.setObjectName("lineEdit_lifetimewin_f")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_lifetimewin_f)
        self.minONlimit_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.minONlimit_label.setObjectName("minONlimit_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.minONlimit_label)
        self.minONlimit_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.minONlimit_lineEdit.setObjectName("minONlimit_lineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.minONlimit_lineEdit)
        self.minNperON_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.minNperON_label.setObjectName("minNperON_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.minNperON_label)
        self.minNperON_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.minNperON_lineEdit.setObjectName("minNperON_lineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.minNperON_lineEdit)
        self.EstimatorButton = QtWidgets.QPushButton(self.ParametergroupBox)
        self.EstimatorButton.setGeometry(QtCore.QRect(60, 340, 141, 34))
        self.EstimatorButton.setObjectName("EstimatorButton")
        self.lifetimeButton = QtWidgets.QPushButton(self.ParametergroupBox)
        self.lifetimeButton.setGeometry(QtCore.QRect(240, 340, 141, 34))
        self.lifetimeButton.setObjectName("lifetimeButton")
        self.Layout.addWidget(self.ParametergroupBox, 0, 1, 1, 1)
        self.Results_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Results_groupBox.setObjectName("Results_groupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Results_groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 441, 411))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.estimateLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.estimateLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.estimateLayout.setContentsMargins(0, 0, 0, 0)
        self.estimateLayout.setObjectName("estimateLayout")
        self.comLabel = QtWidgets.QLabel(self.Results_groupBox)
        self.comLabel.setGeometry(QtCore.QRect(10, 450, 281, 81))
        self.comLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.comLabel.setText("")
        self.comLabel.setTextFormat(QtCore.Qt.AutoText)
        self.comLabel.setObjectName("comLabel")
        self.SaveResultsButton = QtWidgets.QPushButton(self.Results_groupBox)
        self.SaveResultsButton.setEnabled(False)
        self.SaveResultsButton.setGeometry(QtCore.QRect(320, 490, 121, 34))
        self.SaveResultsButton.setObjectName("SaveResultsButton")
        self.CreatepdfcheckBox = QtWidgets.QCheckBox(self.Results_groupBox)
        self.CreatepdfcheckBox.setEnabled(False)
        self.CreatepdfcheckBox.setGeometry(QtCore.QRect(320, 460, 121, 23))
        self.CreatepdfcheckBox.setChecked(True)
        self.CreatepdfcheckBox.setObjectName("CreatepdfcheckBox")
        self.Layout.addWidget(self.Results_groupBox, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionOne = QtWidgets.QAction(MainWindow)
        self.actionOne.setObjectName("actionOne")
        self.actionTwo = QtWidgets.QAction(MainWindow)
        self.actionTwo.setObjectName("actionTwo")
        self.actionThree = QtWidgets.QAction(MainWindow)
        self.actionThree.setObjectName("actionThree")
        self.actionFour = QtWidgets.QAction(MainWindow)
        self.actionFour.setObjectName("actionFour")
        self.actionFive = QtWidgets.QAction(MainWindow)
        self.actionFive.setObjectName("actionFive")
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")

        self.retranslateUi(MainWindow)
        self.LoadPSFButton.clicked.connect(MainWindow.fit_exppsf)
        self.LoadTCSPCButton.clicked.connect(MainWindow.load_tcspc)
        self.browseFileTCSPC.clicked.connect(MainWindow.select_tcspc)
        self.browseFilePSF.clicked.connect(MainWindow.select_exppsf)
        self.psfScrollbar.valueChanged['int'].connect(MainWindow.show_psf)
        self.pushButton_addWindow.clicked.connect(MainWindow.region_selection)
        self.checkBox_TraceSelection.toggled['bool'].connect(MainWindow.check_tcspcmode)
        self.EstimatorButton.clicked.connect(MainWindow.position_estimation)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Analysis"))
        self.TCSPCgroupBox.setTitle(_translate("MainWindow", "TCSPC"))
        self.radioButton_NP.setText(_translate("MainWindow", "Nanoparticle"))
        self.radioButton_origami_manual.setText(_translate("MainWindow", "Origami (manual)"))
        self.radioButton_origami_auto.setText(_translate("MainWindow", "Origami (auto)"))
        self.checkBox_TraceSelection.setText(_translate("MainWindow", "Select window(s)"))
        self.pushButton_addWindow.setText(_translate("MainWindow", "Add window"))
        self.pushButton_saveOntimes.setText(_translate("MainWindow", "Save On-times"))
        self.PushButton_LoadOntimes.setText(_translate("MainWindow", "Load On-times"))
        self.threshold_lineEdit.setText(_translate("MainWindow", "100"))
        self.threshold_label.setText(_translate("MainWindow", "Threshold"))
        self.binWidthlineEdit.setText(_translate("MainWindow", "0.1"))
        self.binWidthlabel.setText(_translate("MainWindow", "Binning [s]"))
        self.PSFgroupBox.setTitle(_translate("MainWindow", "Data"))
        self.PSFfile_groupBox.setTitle(_translate("MainWindow", "PSF file selection"))
        self.browseFilePSF.setText(_translate("MainWindow", "Browse File"))
        self.PSFmode_groupBox.setTitle(_translate("MainWindow", "PSF type"))
        self.radioButton_exppsf.setText(_translate("MainWindow", "Experimental PSF"))
        self.radioButton_psffit.setText(_translate("MainWindow", "PSF fit"))
        self.LoadPSFButton.setText(_translate("MainWindow", "Fit PSF"))
        self.pushButton_saveFit.setText(_translate("MainWindow", "Save Fit"))
        self.TCSPCfile_groupBox.setTitle(_translate("MainWindow", "TCSPC file selection"))
        self.browseFileTCSPC.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select the tcspc file you want to load.</p></body></html>"))
        self.browseFileTCSPC.setText(_translate("MainWindow", "Browse File"))
        self.LoadTCSPCButton.setText(_translate("MainWindow", "Load TCSPC"))
        self.ParametergroupBox.setTitle(_translate("MainWindow", "Parameter"))
        self.label_numPSF.setText(_translate("MainWindow", "# of donut positions"))
        self.label_SBR.setText(_translate("MainWindow", "Background [kHz]"))
        self.lineEdit_sbr.setText(_translate("MainWindow", "16.98"))
        self.label_winlen.setToolTip(_translate("MainWindow", "Only matters if \'Nanoparticle\' mode is used"))
        self.label_winlen.setText(_translate("MainWindow", "Artifical binning [s]"))
        self.lineEdit_winlen.setText(_translate("MainWindow", "0.1"))
        self.label_lifetime_window_i.setText(_translate("MainWindow", "Lifetime init [ns]"))
        self.lineEdit_lifetimewin_i.setText(_translate("MainWindow", "0"))
        self.label_lifetime_window_f.setText(_translate("MainWindow", "Lifetime crop [ns]"))
        self.lineEdit_lifetimewin_f.setText(_translate("MainWindow", "2"))
        self.minONlimit_label.setText(_translate("MainWindow", "Min. ON-time [s]"))
        self.minONlimit_lineEdit.setText(_translate("MainWindow", "0.05"))
        self.minNperON_label.setText(_translate("MainWindow", "Min. Photons per ON"))
        self.minNperON_lineEdit.setText(_translate("MainWindow", "10"))
        self.EstimatorButton.setText(_translate("MainWindow", "Estimate Position"))
        self.lifetimeButton.setText(_translate("MainWindow", "Fit Lifetime"))
        self.Results_groupBox.setTitle(_translate("MainWindow", "Results"))
        self.SaveResultsButton.setText(_translate("MainWindow", "Save Results"))
        self.CreatepdfcheckBox.setText(_translate("MainWindow", "Create .pdf"))
        self.actionOne.setText(_translate("MainWindow", "One"))
        self.actionTwo.setText(_translate("MainWindow", "Two"))
        self.actionThree.setText(_translate("MainWindow", "Three"))
        self.actionFour.setText(_translate("MainWindow", "Four"))
        self.actionFive.setText(_translate("MainWindow", "Five"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.action2.setText(_translate("MainWindow", "2"))
        self.action3.setText(_translate("MainWindow", "3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

