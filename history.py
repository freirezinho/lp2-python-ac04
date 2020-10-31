
class Historico:
    data: str
    horario: str
    observacao: str
    medico: str

    def __init__(self, data: str, horario: str, observacao: str, medico: str):
        self.data = data
        self.horario = horario
        self.observacao = observacao
        self.medico = medico

    def get_data(self):
        return self.data

    def get_horario(self):
        return self.horario

    def get_observacao(self):
        return self.observacao

    def get_medico(self):
        return self.medico
