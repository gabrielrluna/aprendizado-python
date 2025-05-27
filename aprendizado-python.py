print("Hello, World!")

#Atribuindo valores à variáveis

nome = "João da Silva"
idade = 20
email = "joao@gmail.com"

print("Nome: "+nome)
print("Idade: ", idade)

print("")
print("=========")
print("")


#Atribuindo valores a uma mesma variável
a = 1
b = 2
c = a
a = 3
a = "Três"

#Pelo dinamismo das variáveis, é possível atribuir mais valores a uma mesma variável. Ela ficará com o último valor atribuido.

print("A variável 'a' é:", a)
print("A variável 'c' é:", c)
#Aqui, a variável "a" representa o  valor "Três", pois foi o último atribuído.
#Já a variável "c" representa o valor "1", pois esse era o valor quando se atribuiu o "a" a essa variável.

print("")
print("=========")
print("")

#Entrada de Dados: A função "input" sempre retorna uma string
nome = input("Insira seu nome: ")
print("Olá, ",nome," tudo bem?")

print("")
print("=========")
print("")

#Para retornar outros tipos de dados na função "input", basta realizar a conversão.
nome  = input("Insira seu nome: ")
idade = int(input("Insira a sua idade: "))
peso  = float(input("Insira seu peso: "))

print("Nome: ", nome)
print("Idade: ", idade)
print("Peso: ", peso)


print("")
print("=========")
print("")


