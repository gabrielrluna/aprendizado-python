#Estruturas de Repetição

#FOR

soma = 0
for i in (0,1,2,3,4):
    soma = soma + 3
    print(soma)
    
print("----------")

for i in (10,21,32,432,5321):
    print(i)

print("----------")

#FOR usando "range" para delimitar uma sequência

#No exemplo abaixo, ele percorrerá entre 0 a 4, com incremento "1"
for i in range (5):
    print (i)

print("----------")

#A seguir, há a delimitação inicial (primeiro item) e de incremento (último item)
for i in range (4,20,2):
    print (i)
#O loop percorreu entre o 4 e o 20 (sem contar o próprio 20), de 2 em 2.

print("----------")

#Percorrendo String com o FOR

nome = "gabriel"
for i in nome:
    print(i)

print("----------")


#WHILE

contador = 0
while (contador < 5):
       contador+=1
       print(contador)

print("----------")

nome = ""
while True:
    texto = input("Digite um nome ou '0' para encerrar o programa")
    if(texto == "0"):
        print("Programa Finalizado")
        break
    else:
        nome = nome + texto +"\n"

print(nome)

print("----------")



