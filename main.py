from src.bookingRepository import BookingRepositry
from src.service import Service
from src.database import DataBase


def main():
    service = Service(BookingRepositry(db=DataBase()))
    service.execute()


if __name__ == '__main__':
    main()
