from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogWindow(object):
    def setupUi(self, LogWindow):
        LogWindow.setObjectName("LogWindow")
        LogWindow.resize(348, 509)
        self.centralwidget = QtWidgets.QWidget(LogWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 351, 511))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("login.png"))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 220, 221, 21))
        self.lineEdit.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 270, 221, 21))
        self.lineEdit_2.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 360, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.pushButton_2.setObjectName("pushButton_2")
        LogWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogWindow)
        QtCore.QMetaObject.connectSlotsByName(LogWindow)

    def retranslateUi(self, LogWindow):
        _translate = QtCore.QCoreApplication.translate
        LogWindow.setWindowTitle(_translate("LogWindow", "MainWindow"))
        self.pushButton.setText(_translate("LogWindow", "Авторизация"))
        self.pushButton_2.setText(_translate("LogWindow", "English"))
