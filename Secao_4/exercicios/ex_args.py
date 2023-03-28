def multiplicacao(*args):
    total = 1
    for n in args:
        total *= n
    return total

total = multiplicacao(7,7)
print(f'O valor total da multiplicação é: {total}')