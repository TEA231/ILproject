from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfilMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: transparent;\n"
                                      "color: white;\n"
                                      "border: none;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background: transparent;\n"
                                 "color: white;\n"
                                 "border: none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: transparent;\n"
                                   "color: white;\n"
                                   "border: none;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 90, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: transparent;\n"
                                   "color: white;\n"
                                   "border: none;")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 440, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background: transparent;\n"
                                        "color: white;\n"
                                        "border: none;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 761, 511))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("3.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(610, 90, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background: transparent;\n"
                                   "color: white;\n"
                                   "border: none;")
        self.label_5.setObjectName("label_5")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 120, 211, 301))
        self.plainTextEdit.setStyleSheet("background: transparent;\n"
                                         "color: white;\n"
                                         "border: none;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(280, 120, 211, 301))
        self.plainTextEdit_2.setStyleSheet("background: transparent;\n"
                                           "color: white;\n"
                                           "border: none;")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(530, 120, 221, 301))
        self.plainTextEdit_3.setStyleSheet("background: transparent;\n"
                                           "color: white;\n"
                                           "border: none;")
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_4.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        self.label_5.raise_()
        self.plainTextEdit.raise_()
        self.plainTextEdit_2.raise_()
        self.plainTextEdit_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_3.setEnabled(False)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Выйти"))
        self.label.setText(_translate("MainWindow", "\"Лог\""))
        self.label_2.setText(_translate("MainWindow", "Рекорды МК"))
        self.label_3.setText(_translate("MainWindow", "Рекорды СК"))
        self.pushButton_2.setText(_translate("MainWindow", "Выйти в меню"))
        self.label_5.setText(_translate("MainWindow", "Рекорды БК"))
