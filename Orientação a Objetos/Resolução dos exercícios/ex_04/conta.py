class Conta:
    def __init__(self, nome, numero, saldo, limite = 1000.0):
        self.__nome = nome
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
