from .exame_interface import ExameInterface


class AprovaExame:
    def aprovar_solicitacao_exame(self, exame: ExameInterface):
        exame.verifica_condicoes_exame()
        print("Aprova exame")
