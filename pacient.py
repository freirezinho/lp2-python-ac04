from person import Pessoa
from physician import Medico
from history import Historico
from room import Quarto


class Paciente(Pessoa):

    __data_de_nascimento: str = ''
    __endereco: str = ''
    __historico: [Historico] = []
    __internado: bool = False
    __quarto: Quarto = None
    __responsavel: Medico = None

    def __init__(self, nome: str, rg: str, cpf: str, endereco: str, telefone: str, data_nascimento: str, responsavel: Medico):
        super().__init__(nome, rg, cpf, telefone)
        self.__endereco = endereco
        self.__data_nascimento = data_nascimento
        self.__responsavel = responsavel

    def designar_quarto(self, quarto: Quarto) -> None:
        self.__quarto = quarto

    def internar_paciente(self, valor: bool) -> None:
        self.__internado = valor

    def registrar_historico(self, data: str, horario: str, observacao: str, medico: str) -> None:
        novo_registro = Historico(data, horario, observacao, medico)
        self.__historico.append(novo_registro)

    def get_historico(self):
        for registro in self.__historico:
            print("--------------------------")
            print(f'{registro.data} | {registro.horario}')
            print("--------------------------")

            print(f'Observação: {registro.observacao}')
            print(f'Médico: {registro.medico}')
            print("--------------------------")

    def trocar_medico_responsavel(self, medico: Medico) -> None:
        self.__responsavel = medico

    def receber_alta(self, historico: Historico) -> None:
        registro_de_alta = historico
        self.__historico.append(registro_de_alta)
        self.__quarto = None
        self.__responsavel = None
        self.__internado = True
