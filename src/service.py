from src.share.serviceBase import ServiceBase
from src.argumens import Arguments
from src.validations import Validations
from src.share.dto import DTOArguments
from src.bookingRepository import BookingRepositry
from src.bookingHandler import BookingHandler
from src.checkHandler import CheckHandler
from src.helpHandler import HelpHandler


class Service(ServiceBase):
    __dto: DTOArguments = None
    __repository: BookingRepositry

    def __init__(self, repository: BookingRepositry):
        self.__repository = repository

    def execute(self):
        self.__parse()

        try:
            self.__validation()
        except Exception as e:
            print(e)
            return

        dataHandler = [
            BookingHandler(self.__repository),
            CheckHandler(self.__repository),
            HelpHandler(self.__repository),
        ]
        for item in dataHandler:
            item.handle(self.__dto)

    def __parse(self):
        arguments = Arguments()
        self.__dto = arguments.parse()

    def __validation(self):
        validations = Validations(self.__dto)
        validations.check()
