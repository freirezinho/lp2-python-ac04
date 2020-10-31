
class Historico:
    __data: str
    __horario: str
    __observacao: str
    __medico: str

    def __init__(self, data: str, horario: str, observacao: str, medico: str):
        self.__data = data
        self.__horario = horario
        self.__observacao = observacao
        self.__medico = medico
