
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
