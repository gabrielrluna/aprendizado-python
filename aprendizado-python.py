#Operadores Aritméticos

a = 4
b = 2
c = 3

print("O valor de 'a' é: ", a)
print("O valor de 'b' é: ", b)
print("-----------")

soma = a + b
print("Soma: ",soma)

print("-----------")

subtracao = a - b
print("Subtração: ",subtracao)

print("-----------")

multiplicacao = a*b
print("Multiplicação: ",multiplicacao)

print("-----------")

divisao = a/b
print("Divisão: ",divisao)

print("-----------")

potenciaA = a**b
potenciaB = b**a
print("'A' elevado a 'b' é: ", potenciaA)
print("'B' elevado a 'A' é: ", potenciaB)

print("-----------")

divisaoInt = a//b
print("A divisão sem resto é: ", divisaoInt)

print("-----------")

#Operadores Relacionais


if(a==b):
    print("A é igual a B")

if(a!=b):
    print("A é diferente de B")

if(a>b):
    print("A é maior que B")

if(a<b):
    print("A é menor que B")

print("-----------")

#Operadores Lógicos

if(a>b)and(c>b):
    print("A é maior que B e C é maior que B")

if(a>b)or (b>c):
    print("A é maior que B ou B é maior que C")

if not(b>c):
    print("B não e maior que C")

print("-----------")

#Concatenação

a = "João"
b = " Silva"
print(a+b)

print("-----------")




