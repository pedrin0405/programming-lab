#While

#Ex1:

"""
cont = 0
mais5 = 2
total = 0
while cont < 5:
    qt = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))
    print(qt*preco)
    total = total + (qt*preco)
    if preco > 50:
        mais5 = mais5 + 1
    cont = cont + 1
print("Quantidades que foram acima de R$50,00: ", mais5)
print("Total gasto: ", total)
"""

#Ex2: Média de Valores(Idades)

"""
soma_id = 0
cont = 0
while cont < 10:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    soma_id = soma_id + idade
    cont = cont + 1
media = soma_id/cont
print("A média de idades é: ", media)
"""

#Ex3: Maior de Valor (Idade)

"""
velha = 0
nomev = ""
cont = 0 
while cont < 10:
    nome = input("Nome: ")
    idade = int(input("Digite sua idade: "))
    if idade > velha:
        velha = idade
        nomev = nome
    cont = cont + 1
print("A pessoa pessoa mais velha é a: ",nomev, "com:", velha)
"""

#Ex4: Menor de Valor (Idade)

"""
id_nova: 999
nomen = ""
cont = 0 
while cont < 10:
    nome = input("Nome: ")
    idade = int(input("Digite sua idade: "))
    if idade < id_nova:
        id_nova = idade
        nomen = nome
    cont = cont + 1
print("A pessoa pessoa mais nova é a: ",nomen, "com:", id_nova)
"""

#Ex5: Código verifica e diagnóstica se a pessoa está com o peso normal ou fora do peso através do IMC

menor = 999
maior = 0
nome_menor = ""
nome_maior = ""
cont = 0
qt_ps = int(input("Quantas pessoas irão verificar o IMC: "))
while cont < qt_ps: 
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    IMC = peso/(altura**2)
    if IMC < 18.5:
        print(nome, "você está Abaixo do Peso!")
        print("_____________________________________") 
    elif IMC < 25:
        print(nome, "você está Dentro do Peso!")
        print("_____________________________________")
    elif IMC < 30:
        print(nome, "você está Acima do Peso!")
        print("_____________________________________")
    else:
        print(nome, "você está no estado de Obesidade!")
        print("_____________________________________")
    if IMC < menor:
        menor = IMC
        nome_menor = nome
    if IMC > maior:
        maior = IMC
        nome_maior = nome
    cont = cont + 1
if qt_ps >= 2:
    print("____________________________________________________")
    print(nome_menor, "você tem o menor IMC de: ", menor)
    print(nome_maior, "você tem o maior IMC de: ", maior)
    print("____________________________________________________")
