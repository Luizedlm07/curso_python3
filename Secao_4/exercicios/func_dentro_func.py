def criar_calculo(multiplicador):

    def multiplicar(num):
        return multiplicador * num
    
    return multiplicar

duplicar = criar_calculo(2)
triplicar = criar_calculo(3)
quadruplicar = criar_calculo(4)

num_calculado = 3

print(duplicar(num_calculado))
print(triplicar(num_calculado))
print(quadruplicar(num_calculado))

