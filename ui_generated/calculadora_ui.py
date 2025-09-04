# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(330, 400)
        MainWindow.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background: qlineargradient(\n"
"		x1:0, y1:0, x2:0, y2:1,\n"
"		stop:0 rgb(108, 108, 162),\n"
"		stop:1 rgb(58, 54, 70)\n"
"	);\n"
"}\n"
"\n"
"QPushButton {\n"
"	min-height: 50px;\n"
"	max-height: 50px;\n"
"	min-width: 70px;\n"
"	font-size: 18px;\n"
"	font-weight: bold;\n"
"	background-color: rgba(205, 238, 255, 0.3);\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(205, 238, 255, 0.5);\n"
"    border: 2px solid rgba(255, 255, 255, 0.3);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(205, 238, 255, 0.7);\n"
"}\n"
"\n"
"QPushButton#btn_divide,\n"
"#btn_multiply, #btn_minus, #btn_plus {\n"
"	background-color: rgba(140, 161, 255, 0.6);\n"
"}\n"
"\n"
"QPushButton#btn_divide:hover,\n"
"QPushButton#btn_multiply:hover,\n"
"QPushButton#btn_minus:hover,\n"
"QPushButton#btn_plus:hover {\n"
"    background-color: rgba(140, 161, 255, 0.8);\n"
"    border: 2px solid rgba(255, 255, 255, 0.4);\n"
"}\n"
"\n"
"QPushButton#btn_divi"
                        "de:pressed,\n"
"QPushButton#btn_multiply:pressed,\n"
"QPushButton#btn_minus:pressed,\n"
"QPushButton#btn_plus:pressed {\n"
"    background-color: rgba(140, 161, 255, 1.0);\n"
"}\n"
"\n"
"QPushButton#btn_equal {\n"
"	background-color: rgba(188, 235, 255, 0.8);\n"
"}\n"
"\n"
"QPushButton#btn_equal:hover {\n"
"    background-color: rgba(188, 235, 255, 1.0);\n"
"    border: 2px solid rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QPushButton#btn_equal:pressed {\n"
"    background-color: rgba(150, 220, 255, 1.0);\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: rgba(0, 0, 0, 0.7);\n"
"}\n"
"\n"
"QLabel#main_display {\n"
"	min-height: 50px;\n"
"	padding-right: 1px;\n"
"	font: 700 18pt \"Century Schoolbook\";\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QLabel#history_display {\n"
"	padding-right: 7px;\n"
"	max-height: 55px;\n"
"	font: 700 8pt \"Century Schoolbook\";\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.history_display = QLabel(self.centralwidget)
        self.history_display.setObjectName(u"history_display")
        font = QFont()
        font.setFamilies([u"Century Schoolbook"])
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        self.history_display.setFont(font)
        self.history_display.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.history_display)

        self.main_display = QLabel(self.centralwidget)
        self.main_display.setObjectName(u"main_display")
        font1 = QFont()
        font1.setFamilies([u"Century Schoolbook"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(False)
        self.main_display.setFont(font1)
        self.main_display.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.main_display)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.btn_multiply = QPushButton(self.centralwidget)
        self.btn_multiply.setObjectName(u"btn_multiply")
        self.btn_multiply.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon()
        icon.addFile(u"../../../../../music/cancel_151850.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_multiply.setIcon(icon)
        self.btn_multiply.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.btn_multiply, 1, 3, 1, 1)

        self.btn_dot = QPushButton(self.centralwidget)
        self.btn_dot.setObjectName(u"btn_dot")
        self.btn_dot.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.btn_dot, 4, 1, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        self.btn_plus.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u"../../../../../music/add_1237946.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_plus.setIcon(icon1)
        self.btn_plus.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_plus, 3, 3, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_divide = QPushButton(self.centralwidget)
        self.btn_divide.setObjectName(u"btn_divide")
        self.btn_divide.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u"../../../../../music/divide_16396281.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_divide.setIcon(icon2)
        self.btn_divide.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_divide, 0, 3, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_clear.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_clear, 0, 0, 1, 1)

        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setObjectName(u"btn_minus")
        self.btn_minus.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon3 = QIcon()
        icon3.addFile(u"../../../../../music/minimize-sign_6057365.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_minus.setIcon(icon3)
        self.btn_minus.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_minus, 2, 3, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.btn_0, 4, 0, 1, 1)

        self.btn_equal = QPushButton(self.centralwidget)
        self.btn_equal.setObjectName(u"btn_equal")
        self.btn_equal.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon4 = QIcon()
        icon4.addFile(u"../../../../../music/equal_149707.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_equal.setIcon(icon4)
        self.btn_equal.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_equal, 4, 2, 1, 2)

        self.btn_percent = QPushButton(self.centralwidget)
        self.btn_percent.setObjectName(u"btn_percent")
        self.btn_percent.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon5 = QIcon()
        icon5.addFile(u"../../../../../music/percent_6839914.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_percent.setIcon(icon5)
        self.btn_percent.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_percent, 0, 2, 1, 1)

        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon6 = QIcon()
        icon6.addFile(u"../../../../../music/backspace_12920795.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete.setIcon(icon6)
        self.btn_delete.setIconSize(QSize(35, 35))

        self.gridLayout.addWidget(self.btn_delete, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.history_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.main_display.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_multiply.setText("")
        self.btn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_plus.setText("")
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_divide.setText("")
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_minus.setText("")
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_equal.setText("")
        self.btn_percent.setText("")
        self.btn_delete.setText("")
    # retranslateUi

