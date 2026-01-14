frase = """O presidente do Vasco, Pedrinho, confirmou que o clube formalizou uma proposta pelo atacante Brenner, atualmente na Udinese, da Itália. Em entrevista à ESPN, o dirigente detalhou o estágio da negociação e destacou o desejo do jogador como um fator positivo, embora tenha ressaltado as dificuldades financeiras envolvidas no processo."""

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)