class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        self.__peso = peso

    def imprime_dados(self):
        print(f'{self.__nome} tem {self.__idade} anos, {self.__altura} de altura e pesa {self.__peso}kg.')

    def calcula_imc(self):
        imc = self.__peso / (self.__altura * self.__altura)
        imc = round(imc, 2)
        print(f'Seu imc é: {imc}')
