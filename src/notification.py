import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.share.dto import DTOArguments


class Notification:
    __sender_email: str
    __sender_password: str
    __subject: str
    __server_smtp_ssl: str
    __port: int

    def __init__(
        self,
        sender_email: str,
        sender_password: str,
        subject: str,
        server_smtp_ssl: str,
        port: int
    ):
        self.__sender_email = sender_email
        self.__sender_password = sender_password
        self.__subject = subject
        self.__server_smtp_ssl = server_smtp_ssl
        self.__port = port

    def send(self, dto: DTOArguments):
        self.__email(dto)

    def __email(self, dto):
        body = f"Кабинет {dto.room} забронирован с {dto.start_datetime} по {dto.end_datetime}"

        message = MIMEMultipart()
        message["From"] = self.__sender_email
        message["To"] = dto.email
        message["subject"] = self.__subject
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP_SSL(self.__server_smtp_ssl, self.__port) as server:
                server.login(self.__sender_email, self.__sender_password)
                server.sendmail(
                    self.__sender_email,
                    dto.email,
                    message.as_string()
                )
            print(
                f"Email sent to {dto.email}: Кабинет {dto.room} забронирован с {dto.start_datetime} по {dto.end_datetime}"
            )
        except Exception as e:
            print(f"Ошибка: {e}")
