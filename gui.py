# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1067, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("QWidget#frmLogin,QWidget#frmPopup,QWidget#frmHostInfo,QWidget#frmLogout,QWidget#frmConfig,QWidget#frmData,QWidget#frmDefence,QWidget#frmHost,QWidget#frmMain,QWidget#frmPwd,QWidget#frmSelect,QWidget#frmMessageBox{\n"
"    border:1px solid #1B89CA;\n"
"    border-radius:0px;    \n"
"}\n"
"\n"
".QFrame{\n"
"    border:1px solid #5CACEE;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QWidget#widget_title{\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5);\n"
"}\n"
"\n"
"QLabel#lab_Ico,QLabel#lab_Title{\n"
"    border-radius:0px;\n"
"    color: #F0F0F0;\n"
"    background-color:rgba(0,0,0,0);\n"
"    border-style:none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #5CACEE;\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"    background: none;\n"
"    selection-background-color: #1B89CA;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"] { \n"
"    lineedit-password-character: 9679; \n"
"}\n"
"\n"
".QGroupBox{\n"
"    border: 1px solid #5CACEE;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
".QPushButton{\n"
"    border-style: none;\n"
"    border: 0px;\n"
"    color: #F0F0F0;\n"
"    padding: 5px;    \n"
"    min-height: 20px;\n"
"    border-radius:5px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
".QPushButton[focusPolicy=\"0\"] {\n"
"    border-style: none;\n"
"    border: 0px;\n"
"    color: #F0F0F0;\n"
"    padding: 0px;    \n"
"    min-height: 10px;\n"
"    border-radius:3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
".QPushButton:hover{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD);\n"
"}\n"
"\n"
".QPushButton:pressed{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5);\n"
"}\n"
"\n"
"QPushButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{\n"
"    border-radius:0px;\n"
"    color: #F0F0F0;\n"
"    background-color:rgba(0,0,0,0);\n"
"    border-style:none;\n"
"}\n"
"\n"
"QPushButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(25, 134, 199, 0), stop:1 #5CACEE);\n"
"}\n"
"\n"
"QPushButton#btnMenu_Close:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(238, 0, 0, 128), stop:1 rgba(238, 44, 44, 255));\n"
"}\n"
"\n"
"QCheckBox {\n"
"    spacing: 2px; \n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/qss_icons/img_rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/qss_icons/img_rc/checkbox_checked.png); \n"
"}\n"
"\n"
"QRadioButton {\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 15px; \n"
"    height: 15px; \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    image: url(:/qss_icons/img_rc/radio_normal.png); \n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    image: url(:/qss_icons/img_rc/radio_selected.png); \n"
"}\n"
"\n"
"QComboBox,QDateEdit{\n"
"    border-radius: 3px;\n"
"    padding: 1px 10px 1px 5px;\n"
"    border: 1px solid #5CACEE;\n"
"}\n"
"\n"
"QComboBox::drop-down,QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px; \n"
"    border-left-width: 1px;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    border-left-color: #5CACEE;\n"
"}\n"
"\n"
"QComboBox::down-arrow,QDateEdit::down-arrow {\n"
"    image: url(:/qss_icons/img_rc/array_down.png); \n"
"}\n"
"\n"
"QMenu {\n"
"    background-color:#F0F0F0;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QMenu::item {    \n"
"    padding: 2px 12px 2px 12px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color: #FFFFFF;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background: #5CACEE;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    border: 1px solid #5CACEE;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    width: 5px; \n"
"    margin: 0.5px;\n"
"    background-color: #1B89CA;\n"
"}\n"
"\n"
"QSlider::groove:horizontal,QSlider::add-page:horizontal { \n"
"    background: #808080; \n"
"    height: 8px; \n"
"    border-radius: 3px; \n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    height: 8px; \n"
"    border-radius: 3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 13px; \n"
"    margin-top: -3px; \n"
"    margin-bottom: -3px; \n"
"    border-radius: 6px;\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,stop:0.6 #F0F0F0, stop:0.778409 #5CACEE);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5, stop: 0.6 #F0F0F0,stop:0.778409 #1B89CA);\n"
"}\n"
"\n"
"QSlider::groove:vertical,QSlider::sub-page:vertical {\n"
"    background:#808080; \n"
"    width: 8px; \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    width: 8px;\n"
"    border-radius: 3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 14px; \n"
"    margin-left: -3px;\n"
"    margin-right: -3px;\n"
"    border-radius: 6px;\n"
"    background: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5, stop: 0.6 #F0F0F0, stop:0.778409 #5CACEE);\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5, stop: 0.6 #F0F0F0,stop:0.778409 #1B89CA);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width:10px; \n"
"    background-color:rgba(0,0,0,0%); \n"
"    padding-top:10px; \n"
"    padding-bottom:10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height:10px; \n"
"    background-color:rgba(0,0,0,0%); \n"
"    padding-left:10px; padding-right:10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    width:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD); \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    height:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD); \n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    width:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    height:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: bottom; \n"
"    subcontrol-origin: margin;\n"
"    border-image:url(:/qss_icons/img_rc/add-line_vertical.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"    border-image:url(:/qss_icons/img_rc/add-line_horizontal.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: top; \n"
"    subcontrol-origin: margin;\n"
"    border-image:url(:/qss_icons/img_rc/sub-line_vertical.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"    border-image:url(:/qss_icons/img_rc/sub-line_horizontal.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical {\n"
"    width:10px;\n"
"    background: #C0C0C0;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {\n"
"    height:10px;\n"
"    background: #C0C0C0;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    border: 0px ; \n"
"}\n"
"\n"
"QTreeView,QListView,QTableView{\n"
"    border: 1px solid #5CACEE; \n"
"    selection-background-color: #1B89CA;\n"
"    selection-color: #F0F0F0;\n"
"}\n"
"\n"
"QTableView::item:selected, QListView::item:selected, QTreeView::item:selected {\n"
"    color: #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QTableView::item:hover, QListView::item:hover, QTreeView::item:hover {\n"
"    color: #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD); \n"
"}\n"
"\n"
"QTableView::item, QListView::item, QTreeView::item {\n"
"    padding: 5px; \n"
"    margin: 0px; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    padding:3px;\n"
"    margin:0px;\n"
"    color:#F0F0F0;\n"
"    border: 1px solid #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom-left-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    color: #F0F0F0;\n"
"    min-width: 60px;\n"
"    min-height: 20px;\n"
"    padding: 3px 8px 3px 8px;\n"
"    margin:1px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD); \n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QStatusBar::item {\n"
"     border: 1px solid #5CACEE;\n"
"     border-radius: 3px;\n"
"}")
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_4 = QtWidgets.QSplitter(self.tab)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter = QtWidgets.QSplitter(self.splitter_4)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.graph1 = PlotWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph1.sizePolicy().hasHeightForWidth())
        self.graph1.setSizePolicy(sizePolicy)
        self.graph1.setMinimumSize(QtCore.QSize(0, 0))
        self.graph1.setObjectName("graph1")
        self.graph2 = PlotWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph2.sizePolicy().hasHeightForWidth())
        self.graph2.setSizePolicy(sizePolicy)
        self.graph2.setMinimumSize(QtCore.QSize(0, 0))
        self.graph2.setObjectName("graph2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 118, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.Upload = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Upload.sizePolicy().hasHeightForWidth())
        self.Upload.setSizePolicy(sizePolicy)
        self.Upload.setIconSize(QtCore.QSize(41, 27))
        self.Upload.setFlat(True)
        self.Upload.setObjectName("Upload")
        self.horizontalLayout_8.addWidget(self.Upload)
        spacerItem2 = QtWidgets.QSpacerItem(10, 15, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.Plotdata = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Plotdata.sizePolicy().hasHeightForWidth())
        self.Plotdata.setSizePolicy(sizePolicy)
        self.Plotdata.setObjectName("Plotdata")
        self.horizontalLayout_8.addWidget(self.Plotdata)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        spacerItem4 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("")
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(2)
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        self.lcdNumber = QtWidgets.QLCDNumber(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("color: rgb(85, 85, 255);")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber.setLineWidth(25)
        self.lcdNumber.setMidLineWidth(45)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_9.addWidget(self.lcdNumber)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        spacerItem5 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_3.addWidget(self.horizontalSlider)
        spacerItem6 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.SamplingPoints = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SamplingPoints.sizePolicy().hasHeightForWidth())
        self.SamplingPoints.setSizePolicy(sizePolicy)
        self.SamplingPoints.setObjectName("SamplingPoints")
        self.horizontalLayout_5.addWidget(self.SamplingPoints)
        spacerItem8 = QtWidgets.QSpacerItem(46, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem9 = QtWidgets.QSpacerItem(20, 88, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem9)
        self.ShowSampledGraph = QtWidgets.QPushButton(self.layoutWidget)
        self.ShowSampledGraph.setObjectName("ShowSampledGraph")
        self.verticalLayout_3.addWidget(self.ShowSampledGraph)
        self.clearSample = QtWidgets.QPushButton(self.layoutWidget)
        self.clearSample.setObjectName("clearSample")
        self.verticalLayout_3.addWidget(self.clearSample)
        spacerItem10 = QtWidgets.QSpacerItem(20, 228, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem10)
        self.gridLayout_2.addWidget(self.splitter_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem11 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem11)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(231, 51))
        self.lineEdit.setStatusTip("")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(261, 51))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(271, 51))
        self.lineEdit_3.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem12 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem12)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(311, 10))
        self.pushButton_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        spacerItem13 = QtWidgets.QSpacerItem(100, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(164, 146, 255)")
        self.comboBox_5.setDuplicatesEnabled(False)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.setItemText(0, "")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setItemText(2, "")
        self.horizontalLayout_2.addWidget(self.comboBox_5)
        spacerItem14 = QtWidgets.QSpacerItem(348, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem15 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem15)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setMinimumSize(QtCore.QSize(271, 41))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.graph3 = PlotWidget(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph3.sizePolicy().hasHeightForWidth())
        self.graph3.setSizePolicy(sizePolicy)
        self.graph3.setMinimumSize(QtCore.QSize(979, 391))
        self.graph3.setAccessibleName("")
        self.graph3.setObjectName("graph3")
        self.verticalLayout_2.addWidget(self.graph3)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1067, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_2.setBuddy(self.graph3)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.horizontalSlider.valueChanged['int'].connect(self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Upload.setText(_translate("MainWindow", "Upload"))
        self.Plotdata.setText(_translate("MainWindow", "Plot data"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#7f5dc8;\">Frequency</span></p></body></html>"))
        self.SamplingPoints.setText(_translate("MainWindow", "Show Sampling points"))
        self.ShowSampledGraph.setText(_translate("MainWindow", "Show Sampled Graph"))
        self.clearSample.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Sampling"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Frequancy"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Amplitude"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "phase"))
        self.pushButton_7.setText(_translate("MainWindow", "Select Generate Sinusoidal"))
        self.comboBox_5.setPlaceholderText(_translate("MainWindow", "Select Generate Sinusoidal"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "First Sinusoidal selction"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#8f8bff;\"># Signal</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Composer"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())