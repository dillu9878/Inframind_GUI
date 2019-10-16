# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from finalCam import CamMainWindow
from BillingWindow import Ui_Form_B
import os, sys

class Ui_Form(object):

    def camera(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui = CamMainWindow()
        self.ui.show()
        self.count += 1
        print(self.count)
        self.label_2.setText(_translate("Form", str(self.count)))

    def biling(self):
        self.ui = Ui_Form_B()
        self.ui.Form.show()

    def setupUi(self, Form):
        self.count = 0
        Form.setObjectName("Form")
        Form.resize(640, 481)
        Form.setGeometry(-170, -100, 680, 500)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-170, -100, 951, 681))
        self.label.setStyleSheet("image: url(:/new1/linux_debian_brand_logo_spiral_93908_1600x900.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 241, 31))
        font = QtGui.QFont()
        font.setFamily("01 Digit")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(85, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(270, 100, 361, 41))
        self.textEdit.setStyleSheet("\n"
"font: 14pt \"Agency FB\";")
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 270, 191, 91))
        self.label_3.setStyleSheet("image: url(:/new1/goods.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(460, 260, 191, 91))
        self.label_4.setStyleSheet("image: url(:/new1/exit.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(9, 263, 191, 131))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setText("")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.camera)


        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 255, 111, 101))

        self.pushButton_2.setText("")

        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")



        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(270, 260, 131, 98))
        self.label_5.setStyleSheet("image: url(:/new1/cash.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 370, 191, 21))
        font = QtGui.QFont()
        font.setFamily("01 Digit")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(85, 255, 0);")
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 160, 191, 131))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setText("")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")


        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(260, 370, 161, 21))
        font = QtGui.QFont()
        font.setFamily("01 Digit")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(85, 255, 0);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(540, 370, 51, 21))
        font = QtGui.QFont()
        font.setFamily("01 Digit")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(85, 255, 0);")
        self.label_8.setObjectName("label_8")

        ## Biling
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 260, 191, 131))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setText("")
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.clicked.connect(self.biling)



        ## Exit
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 258, 121, 133))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setText("")
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_5.clicked.connect(sys.exit)



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", str(self.count)))
        self.label_6.setText(_translate("Form", "Add a New Product"))
        self.label_7.setText(_translate("Form", "Billing Details"))
        self.label_8.setText(_translate("Form", "Exit"))


import main_ui


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
