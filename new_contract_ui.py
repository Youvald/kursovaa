# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_contract.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 714)
        font = QFont("Tomorrow")
        font.setPointSize(29)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(245, 245, 245)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(60, 30, 386, 96))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Untitled.png"))
        self.logo.setObjectName("logo")
        self.about_us = QtWidgets.QLabel(self.centralwidget)
        self.about_us.setGeometry(QtCore.QRect(480, 40, 321, 81))
        font = QFont("Tomorrow")
        font.setPointSize(36)
        self.about_us.setFont(font)
        self.about_us.setStyleSheet("color: rgb(228, 90, 90);")
        self.about_us.setObjectName("about_us")
        self.support = QtWidgets.QLabel(self.centralwidget)
        self.support.setGeometry(QtCore.QRect(760, 30, 281, 101))
        font = QFont("Tomorrow")
        font.setPointSize(36)
        self.support.setFont(font)
        self.support.setStyleSheet("color: rgb(228, 90, 90);")
        self.support.setObjectName("support")
        self.logout = QtWidgets.QLabel(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(1020, 40, 251, 81))
        font = QFont("Tomorrow")
        font.setPointSize(36)
        self.logout.setFont(font)
        self.logout.setStyleSheet("color: rgb(228, 90, 90);")
        self.logout.setObjectName("logout")
        self.new_contract = QtWidgets.QLabel(self.centralwidget)
        self.new_contract.setGeometry(QtCore.QRect(380, 120, 591, 111))
        font = QFont("Tomorrow")
        font.setPointSize(54)
        self.new_contract.setFont(font)
        self.new_contract.setStyleSheet("color: rgb(228, 90, 90);")
        self.new_contract.setAlignment(QtCore.Qt.AlignCenter)
        self.new_contract.setObjectName("new_contract")
        self.choose_ad_space = QtWidgets.QLabel(self.centralwidget)
        self.choose_ad_space.setGeometry(QtCore.QRect(410, 220, 551, 61))
        font = QFont("OFL Sorts Mill Goudy TT")
        font.setPointSize(24)
        self.choose_ad_space.setFont(font)
        self.choose_ad_space.setStyleSheet("color:rgb(179, 179, 179)")
        self.choose_ad_space.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_ad_space.setObjectName("choose_ad_space")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(440, 280, 481, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.create_contract = QtWidgets.QPushButton(self.centralwidget)
        self.create_contract.setGeometry(QtCore.QRect(890, 600, 220, 72))
        font = QFont("Palanquin dark")
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
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(360, 420, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("start_date")
        self.choose_ad_space_2 = QtWidgets.QLabel(self.centralwidget)
        self.choose_ad_space_2.setGeometry(QtCore.QRect(370, 370, 221, 41))
        font = QFont("OFL Sorts Mill Goudy TT")
        font.setPointSize(24)
        self.choose_ad_space_2.setFont(font)
        self.choose_ad_space_2.setStyleSheet("color:rgb(179, 179, 179)")
        self.choose_ad_space_2.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_ad_space_2.setObjectName("choose_ad_space_2")
        self.choose_ad_space_3 = QtWidgets.QLabel(self.centralwidget)
        self.choose_ad_space_3.setGeometry(QtCore.QRect(710, 370, 221, 41))
        font = QFont("OFL Sorts Mill Goudy TT")
        font.setPointSize(24)
        self.choose_ad_space_3.setFont(font)
        self.choose_ad_space_3.setStyleSheet("color:rgb(179, 179, 179)")
        self.choose_ad_space_3.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_ad_space_3.setObjectName("choose_ad_space_3")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(700, 420, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setObjectName("end_date")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(340, 470, 271, 51))
        font = QFont("Neuton")
        font.setPointSize(24)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.price = QtWidgets.QLabel(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(820, 470, 381, 61))
        font = QFont("Tomorrow SemiBold")
        font.setPointSize(26)
        self.price.setFont(font)
        self.price.setStyleSheet("color: rgb(228, 90, 90);")
        self.price.setObjectName("price")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(920, 540, 141, 51))
        font = QFont("Yanone Kaffeesatz")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.about_us.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">.about-us-NTB</span><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\"> {</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">align-items</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">center;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">color</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">#e45a5a;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">display</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">flex;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">flex-shrink</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">0;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">font-family</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">Tomorrow, \'Source Sans Pro\';</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">font-size</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">4.8rem;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">font-weight</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">400;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">justify-content</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">center;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">line-height</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">0.4791666667;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">white-space</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">nowrap;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">}</span></p></body></html>"))
        self.about_us.setText(_translate("MainWindow", "About us"))
        self.support.setText(_translate("MainWindow", "Support"))
        self.logout.setText(_translate("MainWindow", "Logout"))
        self.new_contract.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">.about-us-NTB</span><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\"> {</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">align-items</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">center;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">color</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">#e45a5a;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">display</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">flex;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">flex-shrink</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">0;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">font-family</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">Tomorrow, \'Source Sans Pro\';</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">font-size</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">4.8rem;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">font-weight</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">400;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">justify-content</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">center;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">line-height</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">0.4791666667;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">white-space</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">nowrap;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">}</span></p></body></html>"))
        self.new_contract.setText(_translate("MainWindow", "New contract"))
        self.choose_ad_space.setText(_translate("MainWindow", "Choose an advertising space"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Metro"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Trasnport"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Radio"))
        self.comboBox.setItemText(3, _translate("MainWindow", "TV"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Billboard"))
        self.create_contract.setText(_translate("MainWindow", "Send"))
        self.choose_ad_space_2.setText(_translate("MainWindow", "Start date"))
        self.choose_ad_space_3.setText(_translate("MainWindow", "End date"))
        self.checkBox.setText(_translate("MainWindow", "I have design"))
        self.price.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">.about-us-NTB</span><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\"> {</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">align-items</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">center;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">color</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">#e45a5a;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">display</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">flex;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">flex-shrink</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">0;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">font-family</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">Tomorrow, \'Source Sans Pro\';</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">font-size</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">4.8rem;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">font-weight</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">400;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">justify-content</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">center;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">line-height</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">0.4791666667;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#c80000;\">white-space</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">: </span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000;\">nowrap;</span></p><p><span style=\" font-family:\'Inter,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">}</span></p></body></html>"))
        self.price.setText(_translate("MainWindow", "Estimated price:"))
        self.label.setText(_translate("MainWindow", "0$"))
