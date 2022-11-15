import sqlite3


class Database:
    def __init__(self):
        # Создание таблицы

        db = sqlite3.connect('database/database.db')
        cursor = db.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            login TEXT,
            time TEXT,
            percent TEXT,
            mode TEXT
        )""")
        db.commit()

    def add(self, login, time, percent, mode):
        self.login = login
        self.time = time
        self.percent = percent
        self.mode = mode
        db = sqlite3.connect('database/database.db')
        cursor = db.cursor()
        cursor.execute(f'INSERT INTO users VALUES (?,?,?,?)', (self.login, self.time, self.percent, self.mode))
        db.commit()
