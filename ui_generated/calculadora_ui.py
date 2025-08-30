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
        MainWindow.resize(326, 400)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"    min-height: 50px;\n"
"    max-height: 50px;\n"
"	min-width: 70px;\n"
"	max-width: 100px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btn_equal {\n"
"	max-width: 220px;\n"
"	background-color: #cdeeff;\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel#main_display {\n"
"	min-height: 50px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.history_display = QLabel(self.centralwidget)
        self.history_display.setObjectName(u"history_display")
        font = QFont()
        font.setPointSize(9)
        self.history_display.setFont(font)
        self.history_display.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.history_display)

        self.main_display = QLabel(self.centralwidget)
        self.main_display.setObjectName(u"main_display")
        font1 = QFont()
        font1.setPointSize(22)
        self.main_display.setFont(font1)
        self.main_display.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.main_display)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.btn_multiply = QPushButton(self.centralwidget)
        self.btn_multiply.setObjectName(u"btn_multiply")

        self.gridLayout.addWidget(self.btn_multiply, 1, 3, 1, 1)

        self.btn_dot = QPushButton(self.centralwidget)
        self.btn_dot.setObjectName(u"btn_dot")

        self.gridLayout.addWidget(self.btn_dot, 4, 1, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")

        self.gridLayout.addWidget(self.btn_plus, 3, 3, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_divide = QPushButton(self.centralwidget)
        self.btn_divide.setObjectName(u"btn_divide")

        self.gridLayout.addWidget(self.btn_divide, 0, 3, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")

        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")

        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")

        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")

        self.gridLayout.addWidget(self.btn_clear, 0, 0, 1, 1)

        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setObjectName(u"btn_minus")

        self.gridLayout.addWidget(self.btn_minus, 2, 3, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")

        self.gridLayout.addWidget(self.btn_0, 4, 0, 1, 1)

        self.btn_equal = QPushButton(self.centralwidget)
        self.btn_equal.setObjectName(u"btn_equal")

        self.gridLayout.addWidget(self.btn_equal, 4, 2, 1, 2)

        self.btn_percent = QPushButton(self.centralwidget)
        self.btn_percent.setObjectName(u"btn_percent")

        self.gridLayout.addWidget(self.btn_percent, 0, 2, 1, 1)

        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")

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
        self.btn_multiply.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.btn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_divide.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

