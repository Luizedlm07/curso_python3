"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")

nomestrip = nome.strip()
nomejoin = ''.join(nomestrip.split())
lennome = len(nomejoin)

if nome and idade:
    if idade.isnumeric() == True and nomejoin.isalpha() == True:
        print(f"Seu nome é: {nomestrip}") 
        print(f"Seu nome invertido é: {nomestrip[::-1]}") 
        if ' ' in nomestrip:
            print(f"Seu nome contém espaço(s)")
        else:
            print("Seu nome NÃO contém espaços") 
        print(f"Seu nome tem {lennome} letras ") 
        print(f"A primeira letra do seu nome é {nomestrip[0]} ") 
        print(f"a última letra do seu nome é: {nomestrip[-1]}")
    else:
        print('Insira as informações corretamente.')
else:
    print('Insira as informações corretamente.')
