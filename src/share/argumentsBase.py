from abc import ABC, abstractmethod
from src.share.dto import DTOArguments


class ArgumentsBase(ABC):

    @abstractmethod
    def parse(self) -> DTOArguments:
        pass
