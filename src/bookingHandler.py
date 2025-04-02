from src.share.handlerBase import HandlerBase
from src.share.enums import CommandsEnum
from src.share.dto import DTOArguments
from src.config import EmailConfig
from src.notification import Notification


class BookingHandler(HandlerBase):
    def handle(self, dto: DTOArguments) -> DTOArguments:
        if dto.command == CommandsEnum.BOOKING.value:
            if self._check_period(dto):
                self._repository.add(dto)
                print("Бронирование успешно создано!")
                email_config = EmailConfig.load_config()
                notification = Notification(
                    sender_email=email_config['sender_email'],
                    sender_password=email_config['password'],
                    subject=email_config['subject'],
                    server_smtp_ssl=email_config['server'],
                    port=email_config['port']
                )
                notification.send(dto)
                print("Уведомление отправлено.")
        return dto
