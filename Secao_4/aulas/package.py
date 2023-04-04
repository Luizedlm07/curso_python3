from sys import path

import modularizacao.aula99
from modularizacao import aula99
from modularizacao.aula99 import *

# from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(modularizacao.aula99.soma_do_modulo(1, 2))
print(aula99.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)