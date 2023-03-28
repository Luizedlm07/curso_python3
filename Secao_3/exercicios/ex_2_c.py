nome = input('Digite seu primeiro nome: ')

nome_curto = len(nome) <= 4
nome_medio = 4 < len(nome) <= 6
nome_longo = 6 < len(nome)

if nome_curto:
    print('Nome curto.')
elif nome_medio:
    print('Nome médio.')
elif nome_longo:
    print('Nome longo.')
