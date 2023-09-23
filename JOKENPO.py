from time import sleep
from random import randint

print('='*10, '\033[1;36mJOKENPO\033[m', '='*10) # Title

itens = ('Pedra', 'Papel', 'Tesoura')
computer = randint(0, 2)
print('''Suas opções:
[ \033[1;36m0\033[m ] Pedra
[ \033[1;36m1\033[m ] Papel
[ \033[1;36m2\033[m ] Tesoura''')
user = int(input('Qual a sua jogada? '))

print(' ')
print('\033[1;31mJO\033[m') # JO - RED
sleep(1)
print('\033[1;33mKEN\033[m') # KEN - YELLOW
sleep(1)
print('\033[1;32mPOOOOO!\033[m') # POOO! - GREEN

print(' ')
print('Computador jogou {}'.format(itens[computer]))
print('Jogador jogou {}'.format(itens[user]))
print(' ')

if computer == 0: # Computador jogou PEDRA
    print('-='*15)
    if user == 0:
        print('EMPATE')
    elif user == 1:
        print('\033[1;32mJOGADOR VENCEU!\033[m') # Jogador Venceu!
    elif user == 2:
        print('\033[1;31mCOMPUTADOR VENCEU!\033[m') # Computador Venceu!
    else:
        print('JOGADA INVÁLIDA!')
    print('-='*15)
        
elif computer == 1: # Computador jogou PAPEL
    print('-='*15)
    if user == 0:
        print('\033[1;31mCOMPUTADOR VENCEU!\033[m') # Computador Venceu!
    elif user == 1:
        print('EMPATE')
    elif user == 2:
        print('\033[1;32mJOGADOR VENCEU!\033[m') # Jogador Venceu!
    else:
        print('JOGADA INVÁLIDA!')
    print('-='*15)

elif computer == 2: # Computador jogou TESOURA
    print('-='*15)
    if user == 0:
        print('\033[1;32mJOGADOR VENCEU!\033[m') # Jogador Venceu!
    elif user == 1:
        print('\033[1;31mCOMPUTADOR VENCEU!\033[m') # Computador Venceu!
    elif user == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
    print('-='*15)
print(' ')