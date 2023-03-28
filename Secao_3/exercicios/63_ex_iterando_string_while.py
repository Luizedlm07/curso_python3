nome = input('Digite seu nome: ')

tamanho_nome = len(nome)
cont = 0
add_caracter = ''

while cont < tamanho_nome:    
    add_caracter += f'*{nome[cont]}'
    cont += 1
print(add_caracter)