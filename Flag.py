# correção da AP1 

"""
sal_base = float(input("Salario base: "))
valorcul = float(input("Valor da Cultura: "))
qtcampo = 0
maiorsal = 0
nomemaior = ""
cont = 0
while cont < 30:
    nome = input("Nome: ")
    funcao = input("Função: ")
    if funcao  == "Campo":
        cultura = int(input("Qt de Culturas: "))
        salmensal = sal_base + (valorcul*cultura)
        qtcampo = qtcampo + 1
    else:
        qtequipes = int(input("Qt de equipes: "))
        salmensal = sal_base + (qtequipes*20)
        if salmensal > maiorsal:
            maiorsal = salmensal
            nomemaior = nome
    print("Nome: ", nome, salmensal)
    cont = cont + 1
per = (qtcampo/cont)*100
print(per, "campo")
print("Maior Salário: ",nomemaior)
"""

#Ex 02: Estrutura de FLAG

"""
soma_idade = 0
qt_pessoa = 0
idade = int(input("Idade: "))
while idade > 0:
    sexo = input("Sexo: ")
    soma_idade = soma_idade + idade
    qt_pessoa = qt_pessoa + 1
    idade = int(input("Idade: "))
media = soma_idade/qt_pessoa
print("Media: ", media)
"""

#Ex 03: Se flag for igual a um número negativo

"""
maior = 0
menor = 999

idade = int(input("Idade: "))
while idade >= 0:
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade
    idade = int(input("Nova idade: "))
print("Maior: ", maior)
print("Menor: ", menor)
"""

#Ex 04: Se ninguém tiver a mesma idade

"""
soma = 0 
menor = 0
sexomenor = ""
qt_pessoa = 0
idade = int(input("Idade: "))
while idade > 0:
    sexo = input("Sexo: ")
    soma = soma + idade
    qt_pessoa = qt_pessoa + 1
    if idade < menor:
        menor = idade
        sexomenor = sexo
    idade = int(input("Idade: "))
print("Média: ", soma/qt_pessoa)
print(sexomenor)
"""

#Ex 05: Solicite o usuário e a senha, montrando no final a quantidade de tentativas de senha erradas

"""
senha_v = "1234"
user = input("Usuário: ")
    senha = input("Senha: ")
tentativas = 1
while senha != senha_v:
    print ("Senha inválida!")
    senha = input("Senha: ")
    tentativas = tentativas + 1
print("Tentativas: ", tentativas)

"""

#Ex 06: contação de votos

"""
cand_1 = 0
cand_2 = 0
cand_3 = 0
branco = 0
nulo = 0
qt_ele = 0
ficha = int(input("Número da Ficha: "))
while ficha > 0:
    if ficha == 1:
        cand_1 = cand_1 + 1
    elif ficha == 2:
        cand_2 = cand_2 + 1
    elif ficha == 3:
        cand_3 = cand_3 + 1
    else:
        nulo = nulo + 1
    qt_ele = qt_ele + 1
    ficha = int(input("Número da Ficha: "))
print("Qt Eleitores: ", qt_ele)
print("Não Escolheram: ", nulo+branco)
if cand_1 > cand_2 and cand_1 > cand_3:
    print("Cand. 1 venceu!")
elif cand_2 > cand_1 and cand_2 > cand_3:
    print("Cand. 1 venceu!")
else:
    print("Cand. 3 venceu!")
    
 """      
 
 #Ex 07: 
 
branco = 0
tinto = 0
rose = 0
tipo = input("Tipo de vinho: ")
while tipo == "B" or tipo == "T" or tipo == "R":
     if tipo == "B":
         branco = branco + 1
     elif tipo == "T":
         tinto = tinto + 1
     else:
         rose = rose + 1
     tipo = input("Tipo de vinho: ")
print("Branco: ", branco/100)
print("Tinto: ", tinto/100)
print("Rose: ", rose/100)