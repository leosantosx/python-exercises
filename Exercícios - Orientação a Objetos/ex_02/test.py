"""
Exercício 02
Crie uma classe para representar uma pessoa, com os atributos nome, idade, altura e peso.
essa classe deve ter um metódo que imprime todos os dados e outro metódo que calcula o IMC (Índice de massa corporal)

Ela deve funcionar dessa forma:

from pessoa import Pessoa
p = Pessoa('Leo', 19, 1.69, 70)
p.imprime_dados()
p.calcula_imc()

Imprime:
        >> Leo tem 19 anos, 1.69 de altura e pesa 70kg.
        >> Seu Imc é 24.51

Mãos à obra!

"""

from pessoa import Pessoa

p = Pessoa('Leo', 19, 1.69, 70)
p.imprime_dados()
p.calcula_imc()