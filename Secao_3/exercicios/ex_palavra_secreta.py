palavra = "python"
segredo = ['*', '*', '*', '*', '*', '*']
acabar_jogo = 1
cont_tentativa = 0
tentativa = []

while acabar_jogo:
    
    print('tentativas: ', cont_tentativa)
    entrada = input("Digite uma letra.")
    
    if entrada in tentativa:
        print("Você ja tentou essa letra!")
    elif len(entrada) > 1:
        print("Digite apenas uma letra!")
    else:
        tentativa.append(entrada)
        cont_tentativa += 1
        
        if entrada in palavra:
            
            for i, letra in enumerate(segredo):
                
                if palavra[i] == entrada:
                    print("Acertou!")
                    del segredo[i]
                    segredo.insert(i, entrada)
                    join_segredo = ''.join(segredo)
                    print(join_segredo)
                    
                    if join_segredo == palavra:
                        print(f"PARABÉNS!!! A palavra é: {palavra}")
                        print(f"Você tentou {cont_tentativa} vezes")
                        acabar_jogo = 0
