from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartMenu(object):

    def setupUi(self, StartMenu):
        StartMenu.setObjectName("MainWindow")
        StartMenu.resize(834, 473)
        self.centralwidget = QtWidgets.QWidget(StartMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -20, 911, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("-1.png"))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 30, 661, 171))
        self.textEdit.setStyleSheet("background: transparent;\n"
                                    "color: white;\n"
                                    "border: none;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 220, 661, 91))
        self.textEdit_2.setStyleSheet("background: transparent;\n"
                                      "color: white;\n"
                                      "border: none;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 350, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background: transparent;\n"
                                        "color: white;\n"
                                        "border: none;")
        self.pushButton_2.setObjectName("pushButton_2")
        StartMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartMenu)
        QtCore.QMetaObject.connectSlotsByName(StartMenu)

    def retranslateUi(self, StartMenu):
        _translate = QtCore.QCoreApplication.translate
        StartMenu.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                         "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" "
                                         "/><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\';"
                                         " font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px;"
                                         " margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                                         "\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Результат"))
