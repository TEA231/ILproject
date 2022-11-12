import sqlite3
import sys
import requests
import datetime
from googletrans import Translator
from PyQt5 import QtWidgets

from LogMenu import Ui_LogWindow
from MainMenu import Ui_MainWindow
from ProfilMenu import Ui_ProfilMenu
from StartMenu import Ui_StartMenu
from ResultMenu import Ui_ResultWindow
import config

log = ''
password = ''
date_1 = datetime.datetime.today()
date_2 = datetime.datetime.today()
translator = Translator()
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


# Функция для создания бд пользователя


def bd_create(name, password):
    db = sqlite3.connect('Database.db')
    c = db.cursor()
    c.execute(f"""CREATE TABLE {name}_{password} (
        language text,
        time text,
        word_count text,
        num_correct_words text,
        pr_correct_words text
    )""")
    db.commit()
    db.close()


# Функция открытия окна профиля


def openProfilMenu():
    ProfilMenu.show()
    MainWindow.close()
    db = sqlite3.connect('Database.db')
    ProfilMenu_ui3.plainTextEdit.setEnabled(False)
    c = db.cursor()
    c.execute(F"SELECT * FROM {log}_{password}")
    c_base = c.fetchall()
    ProfilMenu_ui3.plainTextEdit.setPlainText(f'Language, time, number, number_+, % \n')
    for index in c_base:
        ProfilMenu_ui3.plainTextEdit.setPlainText(f'{ProfilMenu_ui3.plainTextEdit.toPlainText()}\n')
        ProfilMenu_ui3.plainTextEdit.setPlainText(f"{ProfilMenu_ui3.plainTextEdit.toPlainText()}"
                                                  f"l: {str(index[0])}; t: {str(index[1])}; n: {str(index[2])};"
                                                  f" n: {str(index[3])}; %: {str(index[4])} \n")
    db.commit()
    db.close()


# Открытие окна главного меню


def openMainWindow():
    MainWindow.show()
    LogWindow.close()
    ProfilMenu.close()
    StartMenu.close()
    ResultMenu.close()


# Открытие главного меню после окна авторизации


def openMainWindow_start():
    db = sqlite3.connect('Database.db')
    c = db.cursor()
    c.execute("SELECT * FROM users")
    items = c.fetchall()
    if len(items) != 0:
        for index in items:
            if LogWindow_ui.lineEdit.text() in index:
                db.close()
                ProfilMenu_ui3.label.setText(LogWindow_ui.lineEdit.text())
                LogWindow_ui.lineEdit.setText('')
                LogWindow_ui.lineEdit_2.setText('')
                return openMainWindow()

        b1 = """INSERT INTO users VALUES (?, ?);"""
        b2 = (LogWindow_ui.lineEdit.text(), LogWindow_ui.lineEdit_2.text())
        c.execute(b1, b2)
        db.commit()
        db.close()
        bd_create(LogWindow_ui.lineEdit.text(), LogWindow_ui.lineEdit_2.text())
        ProfilMenu_ui3.label.setText(LogWindow_ui.lineEdit.text())
        LogWindow_ui.lineEdit.setText('')
        LogWindow_ui.lineEdit_2.setText('')
        return openMainWindow()
    else:
        b1 = """INSERT INTO users VALUES (?, ?);"""
        b2 = (LogWindow_ui.lineEdit.text(), LogWindow_ui.lineEdit_2.text())
        c.execute(b1, b2)
        db.commit()
        db.close()
        bd_create(LogWindow_ui.lineEdit.text(), LogWindow_ui.lineEdit_2.text())
        ProfilMenu_ui3.label.setText(LogWindow_ui.lineEdit.text())
        log = LogWindow_ui.lineEdit.text()
        password = LogWindow_ui.lineEdit_2.text()
        LogWindow_ui.lineEdit.setText('')
        LogWindow_ui.lineEdit_2.setText('')
        return openMainWindow()


# Открытие окна старт


def openStartMenu():
    StartMenu.show()
    MainWindow.close()
    date_1 = datetime.datetime.today()

    # Парсинг текста
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
    number_true_words = 0
    text_test_2 = StartMenu_ui4.textEdit_2.toPlainText()
    date_2 = datetime.datetime.today()
    date3 = date_2 - date_1
    if LogWindow_ui.pushButton_2.text() == 'English':
        ResultWindow_ui.label_3.setText("Язык текста: Русский.")
        ResultWindow_ui.label_5.setText(f'Затраченное время: {str(date3.seconds)} секунд.')
        ResultWindow_ui.label_4.setText(f'Количество слов: {len(config.text_test.split())}.')
        for index in config.text_test.split():
            if index in text_test_2.split():
                number_true_words += 1
        ResultWindow_ui.label_6.setText(f'Количество правильно введеных слов: {str(number_true_words)}.')
        percent_true_words = 100 // len(config.text_test.split()) * number_true_words
        ResultWindow_ui.label_2.setText(f'Процент правильно введеных слов: {percent_true_words}%.')
    else:
        ResultWindow_ui.label_3.setText("Text language: Russian.")
        ResultWindow_ui.label_5.setText(f'Time: {str(date3.seconds)} seconds.')
        ResultWindow_ui.label_4.setText(f'Number of words: {len(config.text_test.split())}.')
        for index in config.text_test.split():
            if index in text_test_2.split():
                number_true_words += 1
        ResultWindow_ui.label_6.setText(f'Number of correctly entered words: {str(number_true_words)}.')
        percent_true_words = 100 // len(config.text_test.split()) * number_true_words
        ResultWindow_ui.label_2.setText(f'Percentage of correctly entered words: {percent_true_words}%.')
    StartMenu_ui4.textEdit_2.setText('')
    db = sqlite3.connect('Database.db')
    c = db.cursor()
    c.execute(F"INSERT INTO {log}_{password} VALUES ('Russian', {str(date3.seconds)},"
              F" {len(config.text_test.split())}, {str(number_true_words)}, {percent_true_words})")
    db.commit()
    db.close()

# Открытие окна авторизации


def openLogMenu():
    LogWindow.show()
    ProfilMenu.close()


# Языковой перевод интерфейса

def language():
    if LogWindow_ui.pushButton_2.text() == 'English':
        # Перевод на Английский
        LogWindow_ui.pushButton_2.setText('Русский')
        MainWindow_ui2.pushButton.setText('Русский')
        LogWindow_ui.pushButton.setText('Authorization')
        MainWindow_ui2.pushButton_8.setText('Profile')
        MainWindow_ui2.pushButton_4.setText('Exit')
        MainWindow_ui2.pushButton_3.setText('Start')
        MainWindow_ui2.pushButton_5.setText(config.quantity_english[config.quantity_num - 1])
        MainWindow_ui2.pushButton_2.setText(config.language_in_test_E[config.language_in_test_num - 1])
        MainWindow_ui2.label.setText('Language')
        MainWindow_ui2.label_2.setText('Language test')
        MainWindow_ui2.label_3.setText('Number of words')
        ProfilMenu_ui3.pushButton.setText('Exit')
        ProfilMenu_ui3.pushButton_2.setText('Exit in menu')
        ProfilMenu_ui3.label_3.setText('Records')
        ProfilMenu_ui3.label_2.setText('Journal')
        StartMenu_ui4.pushButton_2.setText('Result')

    else:
        # Перевод на Русский
        LogWindow_ui.pushButton_2.setText('English')
        MainWindow_ui2.pushButton.setText('English')
        LogWindow_ui.pushButton.setText('Авторизация')
        MainWindow_ui2.pushButton_8.setText('Профиль')
        MainWindow_ui2.pushButton_4.setText('Выход')
        MainWindow_ui2.pushButton_3.setText('Старт')
        MainWindow_ui2.pushButton_5.setText(config.quantity_russian[config.quantity_num - 1])
        MainWindow_ui2.pushButton_2.setText(config.language_in_test_R[config.language_in_test_num - 1])
        MainWindow_ui2.label.setText('Язык')
        MainWindow_ui2.label_2.setText('Язык в тесте')
        MainWindow_ui2.label_3.setText('Количество слов')
        ProfilMenu_ui3.pushButton.setText('Выйти')
        ProfilMenu_ui3.pushButton_2.setText('Выйти в меню')
        ProfilMenu_ui3.label_3.setText('Рекорды')
        ProfilMenu_ui3.label_2.setText('Журнал')
        StartMenu_ui4.pushButton_2.setText('Результат')


# Смена режима количества текста

def quantity():
    if config.quantity_num == 1 or config.quantity_num == 2:
        config.quantity_num += 1
        if LogWindow_ui.pushButton_2.text() == 'Русский':
            MainWindow_ui2.pushButton_5.setText(config.quantity_english[config.quantity_num - 1])
        else:
            MainWindow_ui2.pushButton_5.setText(config.quantity_russian[config.quantity_num - 1])
    else:
        config.quantity_num = 1
        if LogWindow_ui.pushButton_2.text() == 'Русский':
            MainWindow_ui2.pushButton_5.setText(config.quantity_english[config.quantity_num - 1])
        else:
            MainWindow_ui2.pushButton_5.setText(config.quantity_russian[config.quantity_num - 1])


# Смена языка в тесте


def language_in_test():
    if config.language_in_test_num == 1:
        config.language_in_test_num = 2
        if LogWindow_ui.pushButton_2.text() == 'Русский':
            MainWindow_ui2.pushButton_2.setText(config.language_in_test_E[config.language_in_test_num - 1])
        else:
            MainWindow_ui2.pushButton_2.setText(config.language_in_test_R[config.language_in_test_num - 1])
    else:
        config.language_in_test_num = 1
        if LogWindow_ui.pushButton_2.text() == 'Русский':
            MainWindow_ui2.pushButton_2.setText(config.language_in_test_E[config.language_in_test_num - 1])
        else:
            MainWindow_ui2.pushButton_2.setText(config.language_in_test_R[config.language_in_test_num - 1])


ResultWindow_ui.pushButton.clicked.connect(openMainWindow)
StartMenu_ui4.pushButton_2.clicked.connect(openResultMenu)
ProfilMenu_ui3.pushButton_2.clicked.connect(openMainWindow)
ProfilMenu_ui3.pushButton.clicked.connect(openLogMenu)
MainWindow_ui2.pushButton_3.clicked.connect(openStartMenu)
MainWindow_ui2.pushButton_4.clicked.connect(exit)
MainWindow_ui2.pushButton_8.clicked.connect(openProfilMenu)
LogWindow_ui.pushButton.clicked.connect(openMainWindow_start)
LogWindow_ui.pushButton_2.clicked.connect(language)
MainWindow_ui2.pushButton_5.clicked.connect(quantity)
MainWindow_ui2.pushButton_2.clicked.connect(language_in_test)
MainWindow_ui2.pushButton.clicked.connect(language)

sys.exit(app.exec_())
