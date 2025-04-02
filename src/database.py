import sqlite3


class DataBase:
    __db_name = 'bookings.db'

    def create_table(self):
        with sqlite3.connect(self.__db_name) as connect:
            connect.cursor().execute('''CREATE TABLE IF NOT EXISTS bookings
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    room_number INTEGER NOT NULL,
                    user_name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    start_datetime DATETIME NOT NULL,
                    end_datetime DATETIME NOT NULL)''')
            connect.commit()

    def get_cursor(self):
        try:
            connect = sqlite3.connect(self.__db_name)
            return connect.cursor()
        except Exception as e:
            print(e)

    def get_connect(self):
        try:
            connect = sqlite3.connect(self.__db_name)
            return connect
        except Exception as e:
            print(e)
