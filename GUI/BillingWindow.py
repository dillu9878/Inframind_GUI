# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'billing.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys

class Ui_Form_B(object):
    def done(self):
        l = len(os.listdir('./Image/'))
        os.mkdir(f'./Image/customer_id{l + 1}')
        self.Form.close()

    def print(self):
        printer_name = ''
        try:
            os.system("lpr billing.txt")
        except:
            print('printer not found.')

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.Form.setObjectName("Form")
        self.Form.resize(640, 481)
        self.Form.setGeometry(0, 0, 680, 500)
        self.label = QtWidgets.QLabel(self.Form)
        self.label.setGeometry(QtCore.QRect(-170, -100, 951, 681))
        self.label.setStyleSheet("image: url(:/new1/linux_debian_brand_logo_spiral_93908_1600x900.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.Form)
        self.label_3.setGeometry(QtCore.QRect(210, 390, 91, 61))
        self.label_3.setStyleSheet("image: url(:/new1/printer.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Form)
        self.label_4.setGeometry(QtCore.QRect(400, 390, 91, 61))
        self.label_4.setStyleSheet("image: url(:/new1/checked.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.addproductbutton = QtWidgets.QPushButton(self.Form)
        self.addproductbutton.setGeometry(QtCore.QRect(230, 210, 121, 123))
        self.addproductbutton.setAutoFillBackground(False)
        self.addproductbutton.setText("")
        self.addproductbutton.setFlat(True)
        self.addproductbutton.setObjectName("addproductbutton")
        self.label_6 = QtWidgets.QLabel(self.Form)
        self.label_6.setGeometry(QtCore.QRect(230, 450, 61, 21))
        font = QtGui.QFont()
        font.setFamily("01 Digit")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(85, 255, 0);")
        self.label_6.setObjectName("label_6")
        self.print_button = QtWidgets.QPushButton(self.Form)
        self.print_button.setGeometry(QtCore.QRect(210, 390, 91, 81))
        self.print_button.setAutoFillBackground(False)
        self.print_button.setText("")
        self.print_button.setFlat(True)
        self.print_button.setObjectName("print_button")

        self.print_button.clicked.connect(self.print)

        self.label_8 = QtWidgets.QLabel(self.Form)
        self.label_8.setGeometry(QtCore.QRect(420, 450, 51, 21))
        font = QtGui.QFont()
        font.setFamily("01 Digit")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(85, 255, 0);")
        self.label_8.setObjectName("label_8")
        self.done_button = QtWidgets.QPushButton(self.Form)
        self.done_button.setGeometry(QtCore.QRect(400, 388, 91, 84))
        self.done_button.setAutoFillBackground(False)
        self.done_button.setText("")
        self.done_button.setFlat(True)
        self.done_button.setObjectName("done_button")

        self.done_button.clicked.connect(self.done)

        self.kirana_label = QtWidgets.QLabel(self.Form)
        self.kirana_label.setGeometry(QtCore.QRect(160, 20, 361, 61))
        font = QtGui.QFont()
        font.setFamily("01 Digit")
        font.setPointSize(24)
        self.kirana_label.setFont(font)
        self.kirana_label.setStyleSheet("color: rgb(85, 255, 0);")
        self.kirana_label.setObjectName("kirana_label")

        self.text_box_area = QtWidgets.QTextEdit(self.Form)
        self.text_box_area.setGeometry(QtCore.QRect(20, 90, 611, 261))
        self.text_box_area.setAutoFillBackground(True)
        self.text_box_area.setStyleSheet("font: 14pt \"Agency FB\";")
        self.text_box_area.setText("")
        self.text_box_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.text_box_area.setObjectName("text_box_area")


        f = open('./Billing/customer_id1/billing.txt', 'r')
        s = f.read()
        self.text_box_area.setText(s)


        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)

    def retranslateUi(self, F):
        _translate = QtCore.QCoreApplication.translate
        F.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "Print"))
        self.label_8.setText(_translate("Form", "Done"))
        self.kirana_label.setText(_translate("Form", "Kirana Product Billing"))


import main_ui


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_Form_B()
    ui.Form.show()
    sys.exit(app.exec_())
