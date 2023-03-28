frase = ''.join(input('digite uma frase: ').lower().split())
cont = 0
qtde_aparece = 0

while cont < len(frase):
    letra_atual = frase[cont]
    qtde_aparece_atual = frase.count(letra_atual)
    #print(letra_atual, qtde_aparece)

    if qtde_aparece < qtde_aparece_atual:
        qtde_aparece = qtde_aparece_atual
        letra_mais_aparece = letra_atual
    cont += 1
print(letra_mais_aparece, qtde_aparece)
