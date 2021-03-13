# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 445)
        MainWindow.setMinimumSize(QtCore.QSize(500, 445))
        MainWindow.setMaximumSize(QtCore.QSize(500, 445))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Assets/Assets/letter-v-button-of-square-shape-with-one-rounded-corner (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(248, 249, 250);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.WOD = QtWidgets.QGroupBox(self.centralwidget)
        self.WOD.setGeometry(QtCore.QRect(5, 80, 350, 260))
        self.WOD.setBaseSize(QtCore.QSize(1, 1))
        self.WOD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.WOD.setAutoFillBackground(False)
        self.WOD.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"background-color: rgb(248, 249, 250);\n"
"gridline-color: rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.WOD.setObjectName("WOD")
        self.wod_word = QtWidgets.QLabel(self.WOD)
        self.wod_word.setGeometry(QtCore.QRect(10, 20, 211, 40))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.wod_word.setFont(font)
        self.wod_word.setStyleSheet("font: 18pt \"Cambria\";\n"
"color: rgb(0, 0, 127);")
        self.wod_word.setTextFormat(QtCore.Qt.AutoText)
        self.wod_word.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.wod_word.setWordWrap(False)
        self.wod_word.setObjectName("wod_word")
        self.wod_def = QtWidgets.QLabel(self.WOD)
        self.wod_def.setGeometry(QtCore.QRect(10, 150, 330, 110))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.wod_def.setFont(font)
        self.wod_def.setStatusTip("")
        self.wod_def.setStyleSheet("font: 12pt \"Constantia\";\n"
"gridline-color: rgb(170, 170, 255);")
        self.wod_def.setScaledContents(True)
        self.wod_def.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.wod_def.setWordWrap(True)
        self.wod_def.setObjectName("wod_def")
        self.wod_pronunciation = QtWidgets.QLabel(self.WOD)
        self.wod_pronunciation.setGeometry(QtCore.QRect(10, 60, 331, 60))
        self.wod_pronunciation.setStyleSheet("font: italic 12pt \"Times New Roman\";")
        self.wod_pronunciation.setObjectName("wod_pronunciation")
        self.wod_type = QtWidgets.QLabel(self.WOD)
        self.wod_type.setGeometry(QtCore.QRect(10, 120, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.wod_type.setFont(font)
        self.wod_type.setStyleSheet("font: 12pt \"Cambria\";\n"
"border-top:1px solid  rgb(234, 234, 234);")
        self.wod_type.setScaledContents(True)
        self.wod_type.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.wod_type.setObjectName("wod_type")
        self.t2s_button = QtWidgets.QPushButton(self.WOD)
        self.t2s_button.setGeometry(QtCore.QRect(305, 20, 40, 40))
        self.t2s_button.setStyleSheet("border:none")
        self.t2s_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Assets/Assets/baseline_volume_up_black_18dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.t2s_button.setIcon(icon1)
        self.t2s_button.setIconSize(QtCore.QSize(20, 30))
        self.t2s_button.setDefault(True)
        self.t2s_button.setObjectName("t2s_button")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(360, 100, 135, 240))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 116, 238))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background-color: rgb(42, 77, 105);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 bold italic 19pt \"Times New Roman\";\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.homw_button = QtWidgets.QPushButton(self.centralwidget)
        self.homw_button.setGeometry(QtCore.QRect(0, 345, 125, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homw_button.sizePolicy().hasHeightForWidth())
        self.homw_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.homw_button.setFont(font)
        self.homw_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Assets/Assets/home (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homw_button.setIcon(icon2)
        self.homw_button.setIconSize(QtCore.QSize(100, 40))
        self.homw_button.setObjectName("homw_button")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.homw_button)
        self.dictionary_button = QtWidgets.QPushButton(self.centralwidget)
        self.dictionary_button.setGeometry(QtCore.QRect(125, 345, 125, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.dictionary_button.setFont(font)
        self.dictionary_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Assets/Assets/big-dictionary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dictionary_button.setIcon(icon3)
        self.dictionary_button.setIconSize(QtCore.QSize(100, 40))
        self.dictionary_button.setObjectName("dictionary_button")
        self.buttonGroup.addButton(self.dictionary_button)
        self.more_button = QtWidgets.QPushButton(self.centralwidget)
        self.more_button.setGeometry(QtCore.QRect(250, 345, 125, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.more_button.setFont(font)
        self.more_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Assets/Assets/apps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.more_button.setIcon(icon4)
        self.more_button.setIconSize(QtCore.QSize(100, 40))
        self.more_button.setObjectName("more_button")
        self.buttonGroup.addButton(self.more_button)
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(375, 345, 125, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.exit_button.setFont(font)
        self.exit_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Assets/Assets/logout (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(icon5)
        self.exit_button.setIconSize(QtCore.QSize(100, 40))
        self.exit_button.setObjectName("exit_button")
        self.buttonGroup.addButton(self.exit_button)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 80, 135, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VOCA : VBT"))
        self.WOD.setTitle(_translate("MainWindow", "WORD OF THE DAY"))
        self.wod_word.setText(_translate("MainWindow", "Word"))
        self.wod_def.setText(_translate("MainWindow", "defination"))
        self.wod_pronunciation.setText(_translate("MainWindow", "[ pronunciation ]"))
        self.wod_type.setText(_translate("MainWindow", "Type"))
        self.t2s_button.setStatusTip(_translate("MainWindow", "speech"))
        self.label.setText(_translate("MainWindow", "VOCA : VOCABULARY BUILDING TOOL"))
        self.homw_button.setStatusTip(_translate("MainWindow", "Home"))
        self.dictionary_button.setStatusTip(_translate("MainWindow", "Dictionary"))
        self.more_button.setStatusTip(_translate("MainWindow", "More"))
        self.exit_button.setStatusTip(_translate("MainWindow", "Exit"))
        self.label_3.setText(_translate("MainWindow", "RECENT WORDS"))
import Main_rc
