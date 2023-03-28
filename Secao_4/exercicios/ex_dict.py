# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for i, pergunta in enumerate(perguntas):
    print(f"\n{pergunta['Pergunta']}\n")

    for index, alternativa in enumerate(pergunta['Opções']):
        print(f'{index}) {alternativa}')

    resposta_certa = str(perguntas[i]['Opções'].index(perguntas[i]['Resposta']))
    resposta = input('\nResposta: ')
    if resposta == resposta_certa:
        print('\nAcertou!!!')
        acertos += 1
    else:
        print('\nErrou!')

print(f'\nVocê acertou {acertos} vez(es).')
if acertos == 3:
    print('Parabéns! zerou o game!')
elif acertos == 2:
    print('Bom, mas pode melhorar!')
elif acertos == 1:
    print('Ok, treine um pouco mais.')
else:
    print('Você foi péssimo.')


