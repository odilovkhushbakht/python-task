from enum import Enum


class CommandsEnum(Enum):
    CHECK = 'check'
    BOOKING = 'booking'
    HELP = 'help'


class ArgumentsEnum(Enum):
    ROOM = 'room'
    NAME = 'name'
    PHONE = 'phone'
    EMAIL = 'email'
    START_DATETIME = 'start_datetime'
    END_DATETIME = 'end_datetime'
