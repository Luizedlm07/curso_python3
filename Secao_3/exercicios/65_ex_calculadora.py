

while True:
    numero_1 = input('Digite o 1º número: ')
    numero_2 = input('Digite o 2º número: ')
    verificador_numeros = numero_1.isdigit() and numero_2.isdigit()

    if verificador_numeros:
        float_numero_1 = float(numero_1)
        float_numero_2 = float(numero_2)
        operadores_permitidos = '+-*/'
        operador = input ('Digite um operador (+-*/): ')

        if operador in operadores_permitidos and len(operador) == 1:

            if operador == '+':
                adicao = float_numero_1 + float_numero_2
                print(adicao)
            if operador == '-':
                subtracao = float_numero_1 - float_numero_2
                print(subtracao)
            if operador == '*':
                multiplicacao = float_numero_1 * float_numero_2
                print(multiplicacao)
            if operador == '/':
                divisao = float_numero_1 / float_numero_2
                print(divisao)
        else:
            print('Digite apenas um operador válido')
            continue
    else:
        print('Digite apenas números')
        continue

    sair = input('Digite [s] para sair: ').lower()
    if sair == 's':
        break

