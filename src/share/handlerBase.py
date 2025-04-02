from abc import ABC, abstractmethod
from src.share.dto import DTOArguments
from src.bookingRepository import BookingRepositry


class HandlerBase(ABC):
    _repository: BookingRepositry

    def __init__(self, repository: BookingRepositry):
        self._repository = repository

    @abstractmethod
    def handle(self, dto: DTOArguments) -> DTOArguments:
        pass
    
    def _check_period(self, dto: DTOArguments) -> bool:
        if dto.start_datetime >= dto.end_datetime:
            print("Ошибка: время окончания должно быть позже времени начала")
            return False

        conflicting = self._repository.check_booking(dto)

        if conflicting:
            print(f"Кабинет {dto.room} занят в указанное время:")
            for book in conflicting:
                print(f"- Занято {book[2]} от {book[5]} до {book[6]}")
            return False
        else:
            print(
                f"Кабинет {dto.room} свободен с {dto.start_datetime} до {dto.end_datetime}"
            )
            return True
