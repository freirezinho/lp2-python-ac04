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
