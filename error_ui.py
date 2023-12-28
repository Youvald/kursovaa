# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(778, 386)
        self.create_contract = QtWidgets.QPushButton(Dialog)
        self.create_contract.setGeometry(QtCore.QRect(400, 300, 220, 72))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.create_contract.setFont(font)
        self.create_contract.setStyleSheet("QPushButton{\n"
"    background-color:rgb(226, 68, 68);\n"
"    color: rgb(255, 255, 255);\n"
"    border:2px solid rgb(226, 68, 68);\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(226, 68, 68);\n"
"}\n"
"")
        self.create_contract.setObjectName("create_contract")
        self.new_contract = QtWidgets.QLabel(Dialog)
        self.new_contract.setGeometry(QtCore.QRect(110, 0, 591, 111))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.new_contract.setFont(font)
        self.new_contract.setStyleSheet("color: rgb(228, 90, 90);")
        self.new_contract.setAlignment(QtCore.Qt.AlignCenter)
        self.new_contract.setObjectName("new_contract")
        self.create_contract_2 = QtWidgets.QPushButton(Dialog)
        self.create_contract_2.setGeometry(QtCore.QRect(170, 300, 220, 72))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.create_contract_2.setFont(font)
        self.create_contract_2.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    border:2px solid rgb(226, 68, 68);\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(226, 68, 68);\n"
"}\n"
"")
        self.create_contract_2.setObjectName("create_contract_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 110, 451, 161))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.create_contract.setText(_translate("Dialog", "Try again"))
        self.new_contract.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">.about-us-NTB</span><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\"> {</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">align-items</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">center;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">color</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">#e45a5a;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">display</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">flex;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">flex-shrink</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">0;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">font-family</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">Tomorrow, \'Source Sans Pro\';</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">font-size</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">4.8rem;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">font-weight</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">400;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">justify-content</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">center;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">line-height</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">0.4791666667;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">white-space</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">nowrap;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">}</span></p></body></html>"))
        self.new_contract.setText(_translate("Dialog", "Error"))
        self.create_contract_2.setText(_translate("Dialog", "Exit"))
        self.label.setText(_translate("Dialog", "<div align=\"center\">Check the information<br>you entered!"))
