num = int(input('Digite o número: '))

print('''Escolha uma base para conversão:
[ 01 ] converter para BINÁRIO
[ 02 ] converter para OCTAR
[ 03 ] converter para HEXADECIMAL''')

print('-=-'*12)

base = int(input('Sua opção: '))

if base == 1:
    print('-=-'*12)
    print('O número {} convertido é {}'.format(num, bin(num)[2:]))
    print('-=-'*12)
elif base == 2:
    print('-=-'*12)
    print('O número {} convertido é {}'.format(num, oct(num)[2:]))
    print('-=-'*12)
elif base == 3:
    print('-=-'*12)
    print('O número {} convertido é {}'.format(num, hex(num)[2:]))
    print('-=-'*12)