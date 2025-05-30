#Estrutura de Dados - Python

minhaLista=[1,2,3,4,5,6,7,8,9]
listaVariada=[1,"Gabriel",4.1,12]

#Acrescentando item numa lista (append)

listaNomes=[]
listaNomes.append("Gabriel")
listaNomes.append("Marcos")
listaNomes.append("Vinícius")
listaNomes.append("Victor")

print(listaNomes)

print("---------")

#Acessando item da lista

print(listaNomes[2])

print("---------")

for nomes in listaNomes:
    print(nomes)

print("---------")

#Alterando item da lista

listaNomes[1]="Marcela"

print(listaNomes)

print("---------")

#Removendo item da lista (pop)
#Toda vez que o programa é executado, o último item da lista é excluido.

listaNomes.pop()
print(listaNomes)

listaNomes.append("Victor")
listaNomes.append("Vinícius")

print(listaNomes)

print("---------")


#Removendo com "remove"
#Com o "remove", é posssível remover um item específico

listaNomes.remove("Vinícius")
print(listaNomes)

print("---------")

#Tuplas

minhaTupla=(0,1,2,3,4)

print("---------")

#Dicionario

meuDicionario={"nome":"Gabriel","idade":31}

#Para acessar um elemento, basta indicar a chave

print(meuDicionario["nome"])
print(meuDicionario["idade"])

print("---------")

#Para atualizar um elemento, basta indicar a chave e atribuir um novo valor

meuDicionario["idade"] = 32
print(meuDicionario)

print("---------")

#Adicionando item ao Dicionario

meuDicionario["email"] = "teste@teste.com"
meuDicionario["situacao"] = "ativo"

print(meuDicionario)

#Removendo itens de um Dicionario (popitem e pop)
#"popitem" sempre remove o último elemento da sequência

meuDicionario.popitem()
print(meuDicionario)
meuDicionario["situacao"] = "ativo"
print(meuDicionario)

#"pop" remove um item específico
meuDicionario.pop("situacao")
print(meuDicionario)




