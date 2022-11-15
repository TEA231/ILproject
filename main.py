import sqlite3
import sys
import requests
import datetime
import config
from PyQt5 import QtWidgets
from database.db import Database
from LogMenu import Ui_LogWindow
from MainMenu import Ui_MainWindow
from ProfilMenu import Ui_ProfilMenu
from StartMenu import Ui_StartMenu
from ResultMenu import Ui_ResultWindow
from operator import itemgetter

app = QtWidgets.QApplication(sys.argv)

# Окно авторизации
LogWindow = QtWidgets.QMainWindow()
LogWindow_ui = Ui_LogWindow()
LogWindow_ui.setupUi(LogWindow)

# Окно главного меню
MainWindow = QtWidgets.QMainWindow()
MainWindow_ui2 = Ui_MainWindow()
MainWindow_ui2.setupUi(MainWindow)

# Окно Профиля
ProfilMenu = QtWidgets.QMainWindow()
ProfilMenu_ui3 = Ui_ProfilMenu()
ProfilMenu_ui3.setupUi(ProfilMenu)

# Окно страта
StartMenu = QtWidgets.QMainWindow()
StartMenu_ui4 = Ui_StartMenu()
StartMenu_ui4.setupUi(StartMenu)

# Окно результата
ResultMenu = QtWidgets.QMainWindow()
ResultWindow_ui = Ui_ResultWindow()
ResultWindow_ui.setupUi(ResultMenu)

# Запуск окна авторизации
LogWindow.show()


# Функция обработки Результата


def word_processing():
    config.date2 = datetime.datetime.now()
    config.time = config.date2 - config.date1
    config.time = int(config.time.seconds)

    config.text_test_2 = StartMenu_ui4.textEdit_2.toPlainText()

    config.num_words = len(config.text_test.split())

    config.correct_num_words = 0
    for index in config.text_test.split():
        if index in config.text_test_2.split():
            config.correct_num_words += 1

    try:
        config.proc_correct_num_words = int(100 // (config.num_words / config.correct_num_words))
    except ZeroDivisionError:
        config.proc_correct_num_words = 0
    StartMenu_ui4.textEdit_2.setText('')
    # Вызов функции для записи результата в базу данных
    db = Database()
    db.add(config.log, config.time, config.proc_correct_num_words, config.quantity_num)


# Сортировка списков
def list_sorted(list1):
    sorted(list1, key=itemgetter(1))
    list1.reverse()
    list2 = []
    for index in list1:
        if index[1] == 100:
            list2.append(index)
            list1.remove(index)
    sorted(list2, key=itemgetter(2))
    for index in list1:
        list2.append(index)
    return list2

# Функция открытия окна профиля


def openProfilMenu():
    db = sqlite3.connect('database/database.db')
    cursor = db.cursor()

    easy_mode_names = []
    medium_mode_names = []
    hard_mode_names = []

    for lvl in cursor.execute(f'SELECT * FROM users'):
        if lvl[3] == "1":
            easy_mode_names.append([lvl[0], lvl[2], lvl[1]])
        elif lvl[3] == "2":
            medium_mode_names.append([lvl[0], lvl[2], lvl[1]])
        elif lvl[3] == "3":
            hard_mode_names.append([lvl[0], lvl[2], lvl[1]])

    easy_mode_names = list_sorted(easy_mode_names)
    medium_mode_names = list_sorted(medium_mode_names)
    hard_mode_names = list_sorted(hard_mode_names)

    number = 0
    ProfilMenu_ui3.plainTextEdit.clear()
    for index in easy_mode_names:
        print(index)
        number += 1
        ProfilMenu_ui3.plainTextEdit.appendHtml('')
        ProfilMenu_ui3.plainTextEdit.appendHtml(f'{number}) Имя: {index[0]} %: {index[1]} время: {index[2]}')

    number = 0
    ProfilMenu_ui3.plainTextEdit_2.clear()
    for index in medium_mode_names:
        number += 1
        ProfilMenu_ui3.plainTextEdit_2.appendHtml('')
        ProfilMenu_ui3.plainTextEdit_2.appendHtml(f'{number}) Имя: {index[0]} %: {index[1]} время: {index[2]}')

    number = 0
    ProfilMenu_ui3.plainTextEdit_3.clear()
    for index in hard_mode_names:
        number += 1
        ProfilMenu_ui3.plainTextEdit_3.appendHtml('')
        ProfilMenu_ui3.plainTextEdit_3.appendHtml(f'{number}) Имя: {index[0]} %: {index[1]} время: {index[2]}')

    ProfilMenu.show()
    MainWindow.close()


# Открытие окна главного меню


def openMainWindow():
    config.log = LogWindow_ui.lineEdit.text()
    ProfilMenu_ui3.label.setText(config.log)
    MainWindow.show()
    LogWindow.close()
    ProfilMenu.close()
    StartMenu.close()
    ResultMenu.close()


# Открытие окна старт


def openStartMenu():
    StartMenu.show()
    MainWindow.close()

    # Парсинг текста
    config.date1 = datetime.datetime.now()
    url = 'https://fish-text.ru/get'

    params = dict(
        type='3',
        number=config.quantity_num * 2,
        format='json'
    )
    resp = requests.get(url=url, params=params)
    data = resp.json()
    config.text_test = str(data['text'])
    StartMenu_ui4.textEdit.setText(data['text'])
    StartMenu_ui4.textEdit.setEnabled(False)


def openResultMenu():

    ResultMenu.show()
    StartMenu.close()
    ResultWindow_ui.label_2.setText(f"Процент правильно введенныых слов: {str(config.proc_correct_num_words)}")
    ResultWindow_ui.label_4.setText(f"Количество слов: {str(config.num_words)}")
    ResultWindow_ui.label_5.setText(f"Затраченное время: {str(config.time)}")
    ResultWindow_ui.label_6.setText(f"Количество правильно введеных слов: {str(config.correct_num_words)}")


# Открытие окна авторизации


def openLogMenu():

    LogWindow.show()
    ProfilMenu.close()
    LogWindow_ui.lineEdit.setText('')


# Смена режима количества текста

def quantity():
    if int(config.quantity_num) == 1 or int(config.quantity_num) == 2:
        config.quantity_num += 1
        MainWindow_ui2.pushButton_5.setText(config.words[config.quantity_num - 1])
    else:
        config.quantity_num = 1
        MainWindow_ui2.pushButton_5.setText(config.words[config.quantity_num - 1])


ResultWindow_ui.pushButton.clicked.connect(openMainWindow)
StartMenu_ui4.pushButton_2.clicked.connect(word_processing)
StartMenu_ui4.pushButton_2.clicked.connect(openResultMenu)
ProfilMenu_ui3.pushButton_2.clicked.connect(openMainWindow)
ProfilMenu_ui3.pushButton.clicked.connect(openLogMenu)
MainWindow_ui2.pushButton_3.clicked.connect(openStartMenu)
MainWindow_ui2.pushButton_4.clicked.connect(exit)
MainWindow_ui2.pushButton_8.clicked.connect(openProfilMenu)
LogWindow_ui.pushButton.clicked.connect(openMainWindow)
MainWindow_ui2.pushButton_5.clicked.connect(quantity)

sys.exit(app.exec_())
