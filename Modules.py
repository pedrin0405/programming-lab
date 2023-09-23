#Quebrando um número


"""
Desafio: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
Ex:
Digite um número: 6.123
O número 6.123 tem a parte inteira 6.

"""

#Com biblioteca
"""
from math import trunc
num = float(input("Digite um Valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, trunc(num)))
"""

#Sem Biblioteca

num = float(input("Digite um Valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, int(num)))




