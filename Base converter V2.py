def convert_base(number, from_base, to_base):
    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return "Bases fora do intervalo (2-36)"
    
    if number == "0":
        return "0"

    # Definindo o conjunto de letras para dígitos maiores que 9.
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Converte o número para a base 10, se não estiver nela.
    if from_base != 10:
        decimal_number = 0
        position = 0
        for digit in number[::-1]:
            decimal_number += digits.index(digit) * (from_base ** position)
            position += 1
    else:
        decimal_number = int(number, 10)

    # Converte o número da base 10 para a base de destino.
    result = ""
    while decimal_number > 0:
        digit = decimal_number % to_base
        result = digits[digit] + result
        decimal_number //= to_base

    return result

# Solicita ao usuário o número e as bases de origem e destino.
number = input("Digite o número a ser convertido (na base atual): ").upper()
from_base = int(input("Digite a base de origem: "))
to_base = int(input("Digite a base de destino: "))

converted_number = convert_base(number, from_base, to_base)
print(f"O número {number} na base {from_base} é igual a {converted_number} na base {to_base}.")
