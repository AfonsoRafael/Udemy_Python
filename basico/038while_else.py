""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        print("Espaco vazio")
        #break

    print(letra)
    i += 1
else: # So é executado esse codigo se sair do while de forma natural, sem break
    print('Não encontrei um espaço na string.')
print('Fora do while.')