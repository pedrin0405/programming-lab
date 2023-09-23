"""
Desafio: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as 
informações positivas sobre ele.

a = input("Digite algo: ")
print("O tipo primitivo desse valor é ", type(a))
print("Só tem espaço: ", a.isspace())
print("É um número: ", a.isnumeric())
print("É Alphabetico: ", a.isalpha())
print("É Alfanúmerico: ", a.isalnum())
print("Está em Maiúscula: ", a.isupper())
print("Está em Minúscula: ", a.islower())
print("Está capitalizada: ", a.istitle())
"""

#Entrada de Valor: Bool, Str, Float, Int

"""
entrada = input('Digite um valor: ')

print('Entrada: ', entrada)

if entrada != "":
    print('Float: ', float(entrada))

print('Bool: ', bool(entrada))
"""

# Tabuada

num = int(input("Digite um número: "))
"""
print('{} x {} = {}'.format(num, 1, num*1))
print('{} x {} = {}'.format(num, 2, num*2))
print('{} x {} = {}'.format(num, 3, num*3))
print('{} x {} = {}'.format(num, 4, num*4))
print('{} x {} = {}'.format(num, 5, num*5))
print('{} x {} = {}'.format(num, 6, num*6))
print('{} x {} = {}'.format(num, 7, num*7))
print('{} x {} = {}'.format(num, 8, num*8))
print('{} x {} = {}'.format(num, 9, num*9))
print('{} x {} = {}'.format(num, 10, num*10))
"""
at_num = int(input("Digite até qual número quer que a tabuada opere: "))
cont = 1
print('-'*12)
while cont < (at_num + 1): 
    print('{} x {:2} = {}'.format(num, cont, num*cont))
    cont = cont + 1
print('-'*12)
