# Sortear um aluno aleátorio 

"""
# import random
from random import choice
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

list = [n1, n2, n3, n4]
#esc = random.choice(list)
esc = choice(list)

print('O aluno escolhido foi: {}'.format(esc))
"""

# Sortear uma ordem dos alunos aleátorio

# import random
from random import shuffle
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

list = [n1, n2, n3, n4]
#random.shuffle(list)
shuffle(list)

print('A ordem de apresentação sera:')
print(list)
