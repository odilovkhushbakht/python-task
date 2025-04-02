import argparse
from src.share.enums import CommandsEnum, ArgumentsEnum
from src.share.dto import DTOArguments
from src.share.argumentsBase import ArgumentsBase


class Arguments(ArgumentsBase):
    __parser = None
    __subparsers = None

    def __init__(self):
        super().__init__()
        self.__parser = argparse.ArgumentParser(
            description='Управление бронированием кабинетов'
        )

        self.__subparsers = self.__parser.add_subparsers(dest='command')

    def parse(self) -> DTOArguments:
        try:
            self.__parse_command_check()
            self.__parse_command_booking()
            self.__parse_command_help()
            return self.__make_dto()
        except argparse.ArgumentError as e:
            print(f"Ошибка аргумента: {e}")
            return DTOArguments(command='help')
        except SystemExit:
            return DTOArguments(command='help')

    def __parse_command_check(self):
        check_parser = self.__subparsers.add_parser(CommandsEnum.CHECK.value)
        check_parser.add_argument(
            ArgumentsEnum.ROOM.value,
            type=int,
            help='Номер кабинета'
        )
        check_parser.add_argument(
            ArgumentsEnum.START_DATETIME.value,
            help='Начало брони (ГГГГ-ММ-ДД ЧЧ:ММ)'
        )
        check_parser.add_argument(
            ArgumentsEnum.END_DATETIME.value,
            help='Конец брони (ГГГГ-ММ-ДД ЧЧ:ММ)'
        )

    def __parse_command_booking(self):
        book_parser = self.__subparsers.add_parser(CommandsEnum.BOOKING.value)
        book_parser.add_argument(
            ArgumentsEnum.ROOM.value,
            type=int,
            help='Номер кабинета'
        )
        book_parser.add_argument(
            ArgumentsEnum.NAME.value,
            type=str,
            help='Ваше имя'
        )
        book_parser.add_argument(
            ArgumentsEnum.EMAIL.value,
            type=str,
            help='Ваш email'
        )
        book_parser.add_argument(
            ArgumentsEnum.PHONE.value,
            type=str,
            help='Ваш телефон'
        )
        book_parser.add_argument(
            ArgumentsEnum.START_DATETIME.value,
            type=str,
            help='Начало брони (ГГГГ-ММ-ДД ЧЧ:ММ)'
        )
        book_parser.add_argument(
            ArgumentsEnum.END_DATETIME.value,
            type=str,
            help='Конец брони (ГГГГ-ММ-ДД ЧЧ:ММ)'
        )

    def __parse_command_help(self):
        self.__subparsers.add_parser(CommandsEnum.HELP.value)

    def __make_dto(self):
        match self.__parser.parse_args().command:
            case CommandsEnum.CHECK.value:
                return DTOArguments(
                    command=self.__parser.parse_args().command,
                    room=self.__parser.parse_args().room,
                    start_datetime=self.__parser.parse_args().start_datetime,
                    end_datetime=self.__parser.parse_args().end_datetime,
                )

            case CommandsEnum.BOOKING.value:
                return DTOArguments(
                    command=self.__parser.parse_args().command,
                    room=self.__parser.parse_args().room,
                    name=self.__parser.parse_args().name,
                    email=self.__parser.parse_args().email,
                    phone=self.__parser.parse_args().phone,
                    start_datetime=self.__parser.parse_args().start_datetime,
                    end_datetime=self.__parser.parse_args().end_datetime,
                )
            case _:
                return DTOArguments(command='help')
