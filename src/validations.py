import re
from datetime import datetime
from src.share.enums import CommandsEnum
from src.share.dto import DTOArguments
from src.share.validationBase import ValidationBase


class Validations(ValidationBase):

    EMAIL_REGEX = re.compile(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    )

    PHONE_REGEX = re.compile(r'^\+?[1-9]\d{7,14}$')
    NAME_REGEX = re.compile(
        r'^[a-zA-Zа-яА-ЯёЁ]{3,}(?:\s+[a-zA-Zа-яА-ЯёЁ]{3,})*$'
    )

    __dto: DTOArguments

    def __init__(self, dto: DTOArguments):
        self.__dto = dto

    def check(self):
        self.__room_number()
        self.__name()
        self.__email()
        self.__phone()
        self.__datetime()

    def __room_number(self):
        if self.__is_not_help():
            if not 1 <= self.__dto.room <= 5:
                raise ValueError("Номер кабинета должен быть от 1 до 5")

    def __name(self):
        if self.__is_booking():
            self.__dto.name = self.__dto.name.strip()
            if not self.__dto.name:
                raise ValueError("Имя не может быть пустым")
            if not self.NAME_REGEX.match(self.__dto.name):
                raise ValueError(
                    "Имя должно содержать минимум 3 буквы (допускаются пробелы между именами)"
                )
            if len(self.__dto.name) > 100:
                raise ValueError("Имя слишком длинное (максимум 100 символов)")

    def __email(self):
        if self.__is_booking():
            if not self.EMAIL_REGEX.match(self.__dto.email):
                raise ValueError("Некорректный формат email")

    def __phone(self):
        if self.__is_booking():
            if not self.PHONE_REGEX.match(self.__dto.phone):
                raise ValueError("Некорректный формат телефона")

    def __datetime(self):
        if self.__is_not_help():
            format = '%Y-%m-%d %H:%M'
            try:
                self.__dto.start_datetime = datetime.strptime(
                    self.__dto.start_datetime,
                    format
                )
                self.__dto.end_datetime = datetime.strptime(
                    self.__dto.end_datetime,
                    format
                )
            except ValueError:
                raise ValueError(
                    "Ошибка формата времени. Используйте ГГГГ-ММ-ДД ЧЧ:ММ"
                )

            now = datetime.now()
            if self.__is_booking() and self.__dto.start_datetime < now:
                raise ValueError("Время начала брони не может быть в прошлом")

    def __is_booking(self) -> bool:
        return self.__dto.command == CommandsEnum.BOOKING.value

    def __is_not_help(self) -> bool:
        return self.__dto.command == CommandsEnum.BOOKING.value or self.__dto.command == CommandsEnum.CHECK.value
