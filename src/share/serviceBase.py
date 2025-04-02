from abc import ABC, abstractmethod


class ServiceBase(ABC):

    @abstractmethod
    def execute(self):
        pass
