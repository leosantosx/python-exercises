from conta import Conta
c = Conta('Maria', '12345', 25.0)

print(f'Nome: {c.nome} - Saldo: {c.saldo} - Limite: {c.limite}')
c.nome = 'Leo'
print(f'Nome: {c.nome} - Saldo: {c.saldo} - Limite: {c.limite}')