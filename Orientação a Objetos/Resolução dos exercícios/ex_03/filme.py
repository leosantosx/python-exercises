class Filme:

    def __init__(self, nome, duracao, ano):
        self.__nome = nome
        self.__duracao = duracao
        self.__ano = ano

    def get_nome(self):
        print(self.__nome)

    def get_duracao(self):
        print(self.__duracao)

    def get_ano(self):
        print(self.__ano)