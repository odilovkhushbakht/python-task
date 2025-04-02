from src.share.repositoryBase import RepositoryBase
from src.database import DataBase


class BookingRepositry(RepositoryBase):
    __db: DataBase = None

    def __init__(self, db: DataBase):
        self.__db = db
        self.__db.create_table()

    def add(self, dto):
        connect = self.__db.get_connect()
        connect.cursor().execute('''INSERT INTO bookings
                        (room_number, user_name, email, phone, start_datetime, end_datetime)
                        VALUES (?, ?, ?, ?, ?, ?)''',
                                 (dto.room, dto.name, dto.email, dto.phone, dto.start_datetime, dto.end_datetime))
        connect.commit()
        connect.close()

    def check_booking(self, dto) -> bool:
        cursor = self.__db.get_cursor()
        cursor.execute(
            '''SELECT * FROM bookings WHERE room_number = ? AND start_datetime < ? AND end_datetime > ? ORDER BY start_datetime''',
            (dto.room, dto.end_datetime, dto.start_datetime)
        )
        return cursor.fetchall()
