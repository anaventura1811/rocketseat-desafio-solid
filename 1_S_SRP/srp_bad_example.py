'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades.
O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única,
organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''


class TaskHandler:
    def conect_api(self):
        pass

    def create_task(self):
        pass

    def update_task(self):
        pass

    def remove_task(self):
        pass

    def send_notification(self):
        pass

    def generate_report(self):
        pass

    def send_report(self):
        pass
