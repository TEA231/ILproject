from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfilMenu(object):
    def setupUi(self, ProfilMenu):
        ProfilMenu.setObjectName("MainWindow")
        ProfilMenu.resize(760, 510)
        self.centralwidget = QtWidgets.QWidget(ProfilMenu)
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
        self.label.setGeometry(QtCore.QRect(20, 10, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(540, 50, 201, 431))
        self.plainTextEdit.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(620, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 280, 171, 201))
        self.plainTextEdit_2.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 250, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 440, 221, 51))
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
        self.label_4.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.plainTextEdit.raise_()
        self.label_2.raise_()
        self.plainTextEdit_2.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        ProfilMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProfilMenu)
        QtCore.QMetaObject.connectSlotsByName(ProfilMenu)

    def retranslateUi(self, ProfilMenu):
        _translate = QtCore.QCoreApplication.translate
        ProfilMenu.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Выйти"))
        self.label.setText(_translate("MainWindow", "\"Лог\""))
        self.label_2.setText(_translate("MainWindow", "Журнал"))
        self.label_3.setText(_translate("MainWindow", "Рекорды"))
        self.pushButton_2.setText(_translate("MainWindow", "Выйти в меню"))
