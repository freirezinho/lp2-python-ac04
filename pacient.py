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
            print(
                f'Data e horário do registro: {registro.data} | {registro.horario}')
            print(f'\nObservação: {registro.observacao}')
            print(f'\nMédico: {registro.medico}')
            print("--------------------------")

    def trocar_medico_responsavel(self, medico: Medico) -> None:
        self.__responsavel = medico

    def receber_alta(self, historico: Historico) -> None:
        registro_de_alta = historico
        self.__historico.append(registro_de_alta)
        self.__quarto = None
        self.__responsavel = None
        self.__internado = True

    def get_nome(self):
        return self.nome

    def set_nome(self):
        self.nome

    def get_rg(self):
        return self.rg

    def set_rg(self):
        self.rg

    def get_cpf(self):
        return self.cpf

    def set_cpf(self):
        self.cpf

    def get_endereco(self):
        return self.endereco

    def set_endereco(self):
        self.endereco

    def get_telefone(self):
        return self.telefone

    def set_telefone(self):
        self.telefone

    def get_data_nascimento(self):
        return self.data_nascimento

    def set_data_nacimento(self):
        self.data_nascimento

    def get_responsavel(self):
        return self.responsavel

    def set_responsavel(self):
        self.responsavel
