from src.share.handlerBase import HandlerBase
from src.share.enums import CommandsEnum
from src.share.dto import DTOArguments


class CheckHandler(HandlerBase):
    def handle(self, dto: DTOArguments) -> DTOArguments:
        if dto.command == CommandsEnum.CHECK.value:
            self._check_period(dto)
        return dto
