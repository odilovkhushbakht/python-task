from abc import ABC, abstractmethod


class ValidationBase(ABC):

    @abstractmethod
    def check(self):
        pass
