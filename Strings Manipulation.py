#Exercise 01: 

"""
name = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(name.upper()))
print('Seu nome em minúscula é {}'. format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(len(name) - name.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(name.find(' ')))
sep = name.split()
print('Seu primeiro nome é {} letras e tem {} letras'.format(sep[0], len(sep[0])))
"""

# Exercise 02:

"""
num = int(input('Informe um número: '))

uni = num//1 % 10
dez = num//10 % 10
cen = num//100 % 10
mil = num//1000 % 10

print('Analisando número: {}'.format(num))
print('Unidade: {}'. format(uni))
print('Dezena: {}'. format(dez))
print('Centena: {}'. format(cen))
print('Milhar: {}'. format(mil))
"""

# Exercise 03:

n = str(input('Digite seu nome completo: ')).strip()
name = n.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(name[0]))
print('Seu último nome é: {}'.format(name[len(name)-1]))

