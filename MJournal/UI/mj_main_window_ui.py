# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mj_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDateEdit, QDateTimeEdit, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QListView,
    QProgressBar, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QTreeView, QVBoxLayout, QWidget)
import mj_main_window_rc
import mj_main_window_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1087, 725)
        Form.setAutoFillBackground(False)
        self.verticalLayout_13 = QVBoxLayout(Form)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/logo/images/bank.png"))

        self.horizontalLayout.addWidget(self.label_3)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.RichText)
        self.label.setScaledContents(False)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_2.setAutoFillBackground(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/icon/images/cal.png"))
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/icon/images/printer.png"))
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout.setStretch(2, 10)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        font2 = QFont()
        font2.setPointSize(10)
        self.tabWidget.setFont(font2)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_17 = QHBoxLayout(self.tab)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox = QComboBox(self.tab)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.tab)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_4.addWidget(self.comboBox_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/logo/images/statistics.png"))

        self.horizontalLayout_5.addWidget(self.label_6)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_14)

        self.label_15 = QLabel(self.tab)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_15)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 6)
        self.horizontalLayout_6.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.label_16 = QLabel(self.tab)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setTextFormat(Qt.RichText)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_16)

        self.label_17 = QLabel(self.tab)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_17)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 6)
        self.horizontalLayout_7.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.line_5 = QFrame(self.tab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.label_18 = QLabel(self.tab)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_18)

        self.label_19 = QLabel(self.tab)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_19)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 6)
        self.horizontalLayout_8.setStretch(2, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.label_20 = QLabel(self.tab)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setTextFormat(Qt.RichText)
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_20)

        self.label_21 = QLabel(self.tab)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_21)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 6)
        self.horizontalLayout_9.setStretch(2, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.line_3 = QFrame(self.tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.progressBar = QProgressBar(self.tab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_10.addWidget(self.progressBar)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.line_4 = QFrame(self.tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.label_22 = QLabel(self.tab)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_22)

        self.label_23 = QLabel(self.tab)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_23)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 6)
        self.horizontalLayout_11.setStretch(2, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_12.addWidget(self.label_13)

        self.label_24 = QLabel(self.tab)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setTextFormat(Qt.RichText)
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_24)

        self.label_25 = QLabel(self.tab)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_25)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 6)
        self.horizontalLayout_12.setStretch(2, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.line_6 = QFrame(self.tab)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_6)

        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setTabShape(QTabWidget.Rounded)
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayoutWidget_4 = QWidget(self.tab_7)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 10, 258, 361))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.treeView = QTreeView(self.verticalLayoutWidget_4)
        self.treeView.setObjectName(u"treeView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.treeView.header().setCascadingSectionResizes(False)
        self.treeView.header().setDefaultSectionSize(100)

        self.verticalLayout_8.addWidget(self.treeView)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.tabWidget_2.addTab(self.tab_10, "")

        self.verticalLayout_7.addWidget(self.tabWidget_2)


        self.horizontalLayout_16.addLayout(self.verticalLayout_7)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.dateEdit = QDateEdit(self.tab)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setCurrentSection(QDateTimeEdit.YearSection)

        self.horizontalLayout_13.addWidget(self.dateEdit)

        self.label_26 = QLabel(self.tab)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setPixmap(QPixmap(u":/icon/images/today.png"))
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_26)

        self.comboBox_3 = QComboBox(self.tab)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_13.addWidget(self.comboBox_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.line_7 = QFrame(self.tab)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_7)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_27 = QLabel(self.tab)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setTextFormat(Qt.RichText)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_27)

        self.label_28 = QLabel(self.tab)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_28)

        self.label_29 = QLabel(self.tab)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_29)

        self.label_30 = QLabel(self.tab)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_30)

        self.label_31 = QLabel(self.tab)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_31)

        self.label_32 = QLabel(self.tab)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_32)

        self.label_33 = QLabel(self.tab)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setTextFormat(Qt.RichText)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_33)


        self.verticalLayout_9.addLayout(self.horizontalLayout_14)

        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        if (self.tableWidget.rowCount() < 6):
            self.tableWidget.setRowCount(6)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(70)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(45)
        self.tableWidget.verticalHeader().setDefaultSectionSize(45)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_9.addWidget(self.tableWidget)


        self.horizontalLayout_15.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 2, -1, -1)
        self.label_34 = QLabel(self.tab)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFrameShape(QFrame.Box)
        self.label_34.setTextFormat(Qt.RichText)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_34)

        self.listView = QListView(self.tab)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_10.addWidget(self.listView)


        self.horizontalLayout_15.addLayout(self.verticalLayout_10)

        self.horizontalLayout_15.setStretch(0, 5)
        self.horizontalLayout_15.setStretch(1, 3)

        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.tabWidget_3 = QTabWidget(self.tab)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.tabWidget_3.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.tabWidget_3.addTab(self.tab_14, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.tabWidget_3.addTab(self.tab_15, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.tabWidget_3.addTab(self.tab_16, "")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.tabWidget_3.addTab(self.tab_17, "")

        self.verticalLayout_11.addWidget(self.tabWidget_3)

        self.verticalLayout_11.setStretch(0, 5)
        self.verticalLayout_11.setStretch(1, 4)

        self.verticalLayout_12.addLayout(self.verticalLayout_11)


        self.horizontalLayout_16.addLayout(self.verticalLayout_12)

        self.horizontalLayout_16.setStretch(0, 3)
        self.horizontalLayout_16.setStretch(1, 10)

        self.horizontalLayout_17.addLayout(self.horizontalLayout_16)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_13.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"MJournal", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#00007f;\">Money Journal V1.00</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4eca\u65e5 2023\u5e74 10\u670825\u65e5\u661f\u671f\u4e09", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"\u6708\u6536\u5165", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"TWD", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u6708\u652f\u51fa", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff0000;\">0</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"TWD", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u5e74\u7d2f\u8a08\u6536\u5165", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"TWD", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u5e74\u7d2f\u8a08\u652f\u51fa", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff0000;\">0</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"TWD", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u672c\u6708\u9810\u7b97", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u9810\u7b97", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"TWD", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u5be6\u969b", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff0000;\">0</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"TWD", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("Form", u"\u5e33\u6236", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("Form", u"\u63d0\u9192", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("Form", u"\u532f\u7387", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), QCoreApplication.translate("Form", u"\u79d1\u76ee", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy\u5e74/M\u6708", None))
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ff0000;\">\u661f\u671f\u65e5</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"\u661f\u671f\u4e00", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"\u661f\u671f\u4e8c", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"\u661f\u671f\u4e09", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"\u661f\u671f\u56db", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"\u661f\u671f\u4e94", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; color:#0000ff;\">\u661f\u671f\u516d</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#00007f;\">2023-10-25</span></p></body></html>", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), QCoreApplication.translate("Form", u"\u672c\u6708\u6536\u652f", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), QCoreApplication.translate("Form", u"\u672c\u6708\u9810\u7b97", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), QCoreApplication.translate("Form", u"\u4ee3\u8fa6\u4ea4\u6613", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), QCoreApplication.translate("Form", u"\u5e33\u6236\u7ba1\u7406", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_15), QCoreApplication.translate("Form", u"\u79d1\u76ee\u7ba1\u7406", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_16), QCoreApplication.translate("Form", u"\u985e\u5225\u7ba1\u7406", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_17), QCoreApplication.translate("Form", u"\u767c\u7968\u5c0d\u734e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u9996\u9801", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u5e33\u52d9\u7d00\u9304", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u9810\u7b97\u8a2d\u5b9a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u6295\u8cc7\u7d00\u9304", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u5831\u8868\u5206\u6790", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Form", u"\u7cfb\u7d71\u8a2d\u5b9a", None))
    # retranslateUi

