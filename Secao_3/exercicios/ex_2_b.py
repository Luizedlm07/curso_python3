hora = input('Que horas são? ')

try:
    hora_de_dormir = 0 <= int(hora) < 6
    bom_dia = 6 <= int(hora) < 12
    boa_tarde = 12 <= int(hora) < 18
    boa_noite = 18 <= int(hora) < 23
    if hora_de_dormir:
        print('Hora de dormir!')    
    elif bom_dia:
        print('Bom dia!')
    elif boa_tarde:
        print('Boa tarde!')
    elif boa_noite:
        print('Boa noite!')
    else:
        print('Essa hora não existe')
except:
    print('Digite a hora como um número inteiro.')

