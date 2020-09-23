"""
Exercício 03

Crie uma classe para representar um filme, com todos atributos privados nome, duração e ano.
essa classe deve ter um metódo get para cada atributo.

Ela deve funcionar dessa forma:

from filme import Filme
f = Filme('Enola Holmes', '2h 3min', 2020)
f.get_nome()
f.get_duração()
f.get_ano()

Imprime:
        >> Enola Holmes
        >> 2h 3min
        >> 2020

Mãos à obra!

"""

from filme import Filme

f = Filme('Enola Holmes', '2h 3min', 2020)
f.get_nome()
f.get_duracao()
f.get_ano()