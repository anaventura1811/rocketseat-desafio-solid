from abc import ABC, abstractmethod


class ExameInterface(ABC):
    def __init__(self, tipo) -> None:
        self.tipo = tipo

    @abstractmethod
    def verifica_condicoes_exame(self, exame): pass
