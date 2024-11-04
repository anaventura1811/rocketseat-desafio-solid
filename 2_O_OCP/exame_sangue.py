from .exame_interface import ExameInterface


class ExameSangue(ExameInterface):
    def verifica_condicoes_exame(self, exame):
        print('Verificando condições exame de sangue')
