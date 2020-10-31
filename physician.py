from person import Pessoa


class Medico(Pessoa):

    __crm: str = ''
    __salario: int = 0
    __especialidades: [str] = []

    def __init__(
        self,
        nome: str,
        rg: str,
        cpf: str,
        crm: str,
        telefone: str,
        salario: int,
        especialidades: [str]
    ):
        super().__init__(nome, rg, cpf, telefone)
        self.__crm = crm
        self.__salario = salario
        self.__especialidades = especialidades

    def get_crm(self) -> str:
        return self.__crm

    def get_especialidade_principal(self) -> str:
        if (len(self.__especialidades) > 0):
            return self.__especialidades[0]
        else:
            return ''

    def get_nome(self) -> str:
        return super().get_nome()

    def get_salario(self) -> int:
        return self.__salario

    def get_todas_especialidades(self) -> [str]:
        return self.__especialidades

    def set_nova_especialidade(self, especialidade: str):
        self.__especialidades.append(especialidade)

    def set_salario(self, valor: int) -> None:
        self.__salario = valor

    def edit_crm(self, crm: str) -> None:
        self.__crm = crm

    def substituir_especialidades(self, especialidades: [str]):
        self.__especialidades = especialidades

    def remover_especialidade(self, especialidade: str) -> None:
        if especialidade in self.__especialidades:
            self.__especialidades.remove(especialidade)
