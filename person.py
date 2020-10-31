from abc import ABC, abstractclassmethod


class Pessoa(ABC):

    __nome: str
    __rg: str
    __cpf: str
    __telefone: str

    def __init__(self, nome: str, rg: str, cpf: str, telefone: str):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome

    def get_rg(self):
        return self.__rg

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self.__telefone

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_rg(self, rg: str):
        self.__rg = rg

    def set_cpf(self, cpf: str):
        self.cpf = cpf

    def set_telefone(self, telefone: str):
        self.__telefone = telefone
