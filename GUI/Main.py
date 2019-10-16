# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abc1.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from finalCam import CamMainWindow
from BillingWindow import Ui_Form_B

class Ui_Form(object):

    def camera(self):
        '''
        f = open('flag.txt', 'w')
        f.write('1')
        f.close()
        '''
        '''
        print('start')
        f = open('flag.txt', 'r')
        s = f.read()
        f.close()
        s = int(s.strip())
        f = open('flag.txt', 'w')
        f.write(str(s + 1))
        f.close()
        '''
        _translate = QtCore.QCoreApplication.translate



        self.ui = CamMainWindow()
        self.ui.show()
        self.count += 1
        '''
        print('close')
        f = open('flag.txt',  'r')
        s = f.read()
        f.close()
        s = s.strip()
        print(s)
        self.count += int(s)
        print(self.count)
        '''
        self.counter_label.setText(_translate("Form", str(self.count)))

    def biling(self):
        self.ui = Ui_Form_B()
        _translate = QtCore.QCoreApplication.translate
        self.ui.Form.show()
        self.count= 0
        self.counter_label.setText(_translate("Form", str(self.count)))

    def create_new(self):
        l = len(os.listdir('./Image/'))
        os.mkdir(f'./Image/customer_id:{l + 1}')

    def __init__(self, Form):
        self.count = 0
        self.create_new()
        Form.setObjectName("Form")
        Form.resize(640, 481)
        Form.setGeometry(-170, -100, 680, 500)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-170, -100, 951, 681))
        self.label.setStyleSheet("image: url(:/new1/linux_debian_brand_logo_spiral_93908_1600x900.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.nofcommodities_label = QtWidgets.QLabel(Form)
        self.nofcommodities_label.setGeometry(QtCore.QRect(10, 100, 241, 31))
        font = QtGui.QFont()
        font.setFamily("01 Digit")
        font.setPointSize(22)
        self.nofcommodities_label.setFont(font)
        self.nofcommodities_label.setStyleSheet("color: rgb(85, 255, 0);")
        self.nofcommodities_label.setObjectName("nofcommodities_label")
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
        self.addproductbutton = QtWidgets.QPushButton(Form)
        self.addproductbutton.setGeometry(QtCore.QRect(9, 263, 191, 131))
        self.addproductbutton.setAutoFillBackground(False)
        self.addproductbutton.setText("")
        self.addproductbutton.setFlat(True)
        self.addproductbutton.setObjectName("addproductbutton")

        self.addproductbutton.clicked.connect(self.camera)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 255, 111, 101))
        self.pushButton_2.setText("")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(Form.close)

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
        '''
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 160, 191, 131))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setText("")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.camera)
        '''

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
        self.billingbutton = QtWidgets.QPushButton(Form)
        self.billingbutton.setGeometry(QtCore.QRect(250, 260, 191, 131))
        self.billingbutton.setAutoFillBackground(False)
        self.billingbutton.setText("")
        self.billingbutton.setFlat(True)
        self.billingbutton.setObjectName("billingbutton")

        self.billingbutton.clicked.connect(self.biling)

        self.exitbutton = QtWidgets.QPushButton(Form)
        self.exitbutton.setGeometry(QtCore.QRect(500, 258, 121, 133))
        self.exitbutton.setAutoFillBackground(False)
        self.exitbutton.setText("")
        self.exitbutton.setFlat(True)
        self.exitbutton.setObjectName("exitbutton")

        self.exitbutton.clicked.connect(Form.close)

        self.counter_label = QtWidgets.QLabel(Form)
        self.counter_label.setGeometry(QtCore.QRect(300, 102, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.counter_label.setFont(font)
        self.counter_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.counter_label.setAutoFillBackground(True)
        self.counter_label.setStyleSheet("")
        self.counter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_label.setObjectName("counter_label")
        self.kirana_label = QtWidgets.QLabel(Form)
        self.kirana_label.setGeometry(QtCore.QRect(160, 20, 361, 61))
        font = QtGui.QFont()
        font.setFamily("01 Digit")
        font.setPointSize(24)
        self.kirana_label.setFont(font)
        self.kirana_label.setStyleSheet("color: rgb(85, 255, 0);")
        self.kirana_label.setObjectName("kirana_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nofcommodities_label.setText(_translate("Form", "No. of Comodities"))
        self.label_6.setText(_translate("Form", "Add a New Product"))
        self.label_7.setText(_translate("Form", "Billing Details"))
        self.label_8.setText(_translate("Form", "Exit"))

        self.counter_label.setText(_translate("Form", "0"))
        self.kirana_label.setText(_translate("Form", "Kirana Product Billing"))


import main_ui


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    #ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
