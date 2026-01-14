"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True # Flag, é uma marcação q muda o valor se
    # entrar no if
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')

print(id(condicao)) # Retorna a posição na memoria
print(id(passou_no_if))
# Curiosidade, se os dois tiverem o msm valor, o local tambem é o msm