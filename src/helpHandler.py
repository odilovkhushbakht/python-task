from src.share.handlerBase import HandlerBase
from src.share.enums import CommandsEnum
from src.share.dto import DTOArguments


class HelpHandler(HandlerBase):
    def handle(self, dto: DTOArguments) -> DTOArguments:
        if dto.command == CommandsEnum.HELP.value:
            print('\n')
            print('Примеры комманд:')
            print('\n')
            print('python main.py booking 1 "Иван" test@mail.ru +79123456789 "2025-05-01 10:00" "2025-05-01 11:00"')
            print('python main.py booking 1 "Анна-Мария" test@mail.ru +79123456789 "2025-05-01 12:00" "2025-05-01 13:00"')
            print('python main.py booking 1 "John Doe" test@mail.ru +79123456789 "2025-05-01 13:00" "2025-05-01 14:00"')
            print('\n')
            print('python main.py check 1 "2025-05-01 10:00" "2025-05-01 11:00"')
            print('python main.py check 1 "2025-05-01 12:00" "2025-05-01 13:00"')
            print('python main.py check 1 "2025-05-01 13:00" "2025-05-01 14:00"')
            print('\n\n')
        return dto
