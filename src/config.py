from dotenv import load_dotenv
import os


class EmailConfig:
    @staticmethod
    def load_config() -> dict:
        load_dotenv()

        config = {
            'sender_email': os.getenv('EMAIL_SENDER'),
            'password': os.getenv('EMAIL_PASSWORD'),
            'server': os.getenv('SMTP_SERVER'),
            'port': os.getenv('SMTP_PORT'),
            'subject': os.getenv('EMAIL_SUBJECT', 'Кабинет забронирован')
        }

        if None in (config['sender_email'], config['password'], config['server']):
            raise ValueError(
                "Не все обязательные email параметры заданы в .env файле")

        try:
            config['port'] = int(config['port']) if config['port'] else 465
        except ValueError:
            raise ValueError("SMTP порт должен быть числом")

        return config
