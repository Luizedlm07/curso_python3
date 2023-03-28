n = input('Digite um número inteiro:')

try:
    n_par = int(n) % 2 == 0
    if n_par:
        print('É par!')
    else:
        print('É ímpar!')
except:
    print('Digite um número inteiro.')
