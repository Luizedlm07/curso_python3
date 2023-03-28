import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

cont = 10
somamulti = 0

for digito in nove_digitos:
    if cont >= 2:
        multi = int(digito) * cont
        somamulti += multi
        cont -= 1
    
calculo_digito1 = (somamulti * 10) % 11
res_digito1 = calculo_digito1 if calculo_digito1 <= 9 else 0
print("Primeiro digito: ", res_digito1)

cont = 11
somamulti = 0
nove_digitos += str(res_digito1)

for digito in nove_digitos:
    if cont >= 2:
        multi = int(digito) * cont
        somamulti += multi
        cont -= 1

calculo_digito2 = (somamulti * 10) % 11
res_digito2 = calculo_digito2 if calculo_digito2 <= 9 else 0
print("Segundo digito: ", res_digito2)

cpf_calculado = nove_digitos[:9] + str(res_digito1) + str(res_digito2)

print(cpf_calculado)
