from datetime import datetime

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def data_nasc(self):
        ano_atual = datetime.today().year
        return ano_atual - self.__idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, nova_altura):
        self.__altura = nova_altura