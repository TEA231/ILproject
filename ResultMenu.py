from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResultWindow(object):
    def setupUi(self, ResultWindow):
        ResultWindow.setObjectName("ResultWindow")
        ResultWindow.resize(628, 368)
        self.centralwidget = QtWidgets.QWidget(ResultWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 30, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 260, 350, 21))
        self.label_2.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 261, 21))
        self.label_3.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 261, 21))
        self.label_4.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 140, 261, 21))
        self.label_5.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 220, 261, 21))
        self.label_6.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 631, 371))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("4.png"))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 312, 571, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: transparent;\n"
"color: white;\n"
"border: none;")
        self.pushButton.setObjectName("pushButton")
        self.label_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        ResultWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ResultWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultWindow)

    def retranslateUi(self, ResultWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultWindow.setWindowTitle(_translate("ResultWindow", "MainWindow"))
        self.label.setText(_translate("ResultWindow", "Результат"))
        self.label_2.setText(_translate("ResultWindow", "Процент правильно введенныых слов: "))
        self.label_3.setText(_translate("ResultWindow", "Язык текста: Русский."))
        self.label_4.setText(_translate("ResultWindow", "Количество слов:"))
        self.label_5.setText(_translate("ResultWindow", "Затраченное время: "))
        self.label_6.setText(_translate("ResultWindow", "Количество правильно введеных слов:"))
        self.pushButton.setText(_translate("ResultWindow", "Ок"))
