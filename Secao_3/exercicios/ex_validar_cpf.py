"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

import re
import sys

entrada_cpf = input("Digite seu CPF: ")
cpf_usuario = re.sub(r'[^0-9]', '', entrada_cpf)
if entrada_cpf[0] * len(entrada_cpf) == entrada_cpf:
    print("CPF inválido. Você digitou uma sequência.")
    sys.exit()

cont = 10
somamulti = 0

for digito in cpf_usuario:
    if cont >= 2:
        multi = int(digito) * cont
        somamulti += multi
        cont -= 1
    
calculo_digito1 = (somamulti * 10) % 11
res_digito1 = calculo_digito1 if calculo_digito1 <= 9 else 0
print("Primeiro digito: ", res_digito1)

cont = 11
somamulti = 0

for digito in cpf_usuario:
    if cont >= 2:
        multi = int(digito) * cont
        somamulti += multi
        cont -= 1

calculo_digito2 = (somamulti * 10) % 11
res_digito2 = calculo_digito2 if calculo_digito2 <= 9 else 0
print("Segundo digito: ", res_digito2)

cpf_calculado = cpf_usuario[:9] + str(res_digito1) + str(res_digito2)

if cpf_usuario == cpf_calculado:
    print(f"O cpf {cpf_usuario} é válido!")
else:
    print(f"O cpf {cpf_usuario} é inválido!")
