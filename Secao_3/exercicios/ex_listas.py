import os

lista_de_compras = []
op = ""
inserir_item = ""
apagar_item = ""



while True:
    op = input("Selecione uma opção:\n[i]nserir, [a]pagar ou [l]istar\n")

    if op != "i" and op != "a" and op != "l":        
        os.system('clear')
        print("Digite uma opção válida")       
        continue

    elif op == "i":
        inserir_item = input("Digite o item para inserir na lista:\n")
        lista_de_compras.append(inserir_item)
        os.system('clear')
        print(f"item {inserir_item} inserido.")

    elif op == "a":

        if lista_de_compras == []:
            os.system('clear')
            print("Você não tem itens na lista.")
            continue

        apagar_item = input("Digite o índice do item que quer apagar:\n")

        if apagar_item.isnumeric():

            if int(apagar_item) < len(lista_de_compras):
                os.system('clear')
                print(f'Item {apagar_item}, {lista_de_compras[int(apagar_item)]} apagado.')
                del lista_de_compras[int(apagar_item)]
            else:
                print("Este item não está na lista.")
                
        else:
            print("Insira um valor válido.")
            os.system('clear')

    elif op == "l":
        if lista_de_compras == []:
            os.system('clear')
            print("Você não tem itens na lista.")
            continue

        for i, item in enumerate(lista_de_compras):
            print(i, item)