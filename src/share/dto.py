from dataclasses import dataclass
from datetime import datetime


@dataclass
class DTOArguments:
    command: str
    room: int = 0
    start_datetime: datetime = None
    end_datetime: datetime = None
    name: str = None
    phone: str = None
    email: str = None
