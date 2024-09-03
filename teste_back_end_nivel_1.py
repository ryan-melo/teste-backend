#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TESTE DE BACKEND NIVEL 1 - GRUPO PEGAZUS

#Faça o teste abaixo 100% sozinho, sem a ajuda de CHAT GPT, amigos, familiares, professores ou etc.. conseguimos facilmente identificar

#lembre-se de detalhar as respostas, assim conseguimos analisar ainda mais o seu conhecimento tecnico

#caso prefira, pode fazer o desafio em outro arquivo separado, e só colar a solução completa abaixo de cada exercicio
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
#Explique detalhadamente por que voce decidiu essa solução e não outra
response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

# Solução:
# primeiramente identifiquei que esse json já foi convertido (não era string json), por isso dispensa pegar a requisição da api e utilizar `json.loads()`

# Solução:
# Aqui aninhei um loop dentro do outro, onde primeiro pego a loja, depois olho cada produto dessa loja,
# quando o valor do produto dor maior que 30, removo ele daquele objeto

for loja in response:
    for j in loja["produtos"]:
        if j["preço"] > 30:
            loja["produtos"].remove(j)

print(response)



#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

# Solução:
# Nesse utilizei a mesma ideia que utilizei no exercício anterior mas nesse ao invés de procurar pelo preço
# procurei pelo nome do produto

for produto in responsejson["produtos"]:
    if produto["nome"] == "Produto B":
        print(produto)


#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]

# Solução:
# Fiz duas soluções, a primeira é por meio de um método já implementado no python:
novaLista = sorted(lista)

# E nessa segunda um algoritmo de ordenação que vi na faculdade mas não me recordo o nome dele:
for i in range(len(lista)):
    index = i
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[index]:
            index = j

    lista[i], lista[index] = lista[index], lista[i]


#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela


lista = ["   joao   ","   maria   ","  joana  "]

# Solução:
# Nesse optei por colocar três soluções:
# Na primeira, onde a lista original é presenrvada, gerando uma nova lista com o que foi pedido e utilizando métodos já implementado:

novaLista = list()

for i in lista:
    novaLista.append(i.strip())

print(novaLista)

# Na segunda, a lista original é modificada, perdendo os valores originais

lista = [i.strip() for i in lista]
print(lista)

# Na terceira sem utilizar métodos prontos:

novaLista = []

for i in lista:
    nome = ""
    for j in i:
        if j != " ":
            nome += j
    novaLista.append(nome)


#5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]

# Solução 1: Utilizando método já implementado
itemRemovido = lista.pop(1)

# Solução 2: Sem utilizar método implementado
novaLista = []

for i in range(len(lista)):
    if i != 1:
        novaLista.append(lista[i])


#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

# Solução 1: Aqui utilizei um conceito do python chamado de compreensão de lista, onde aplico algo para cada item, sem retornar uma nova lista
lista = ["maria" if i == "joao" else i for i in lista]

# Solução 2: Sem o conceito anterior, a solução fica, retornando uma nova lista:

novaLista = []

for i in lista:
    if i == "joao":
        novaLista.append("maria")
    else:
        novaLista.append(i)


#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra

# Solução:
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

count = 0
while count <= 5:
    print(lista[count])
    count += 1

#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra

# Solução: Utilizei a biblioteca requests para fazer a requisição tipo GET na api
# Iniciei dois contadores para tasks completas e imcompletas, respectivamente
# após isso, interei cada objeto procurando pelo "completed"
import requests

completas = 0
incompletas = 0

requisicao = requests.get("https://jsonplaceholder.typicode.com/todos")
print(requisicao)

tasks = requisicao.json()

for i in tasks:
    if i["completed"]:
        completas += 1
    else:
        incompletas += 1

#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra

# Solução: Também utilizei requests, em cada user procuro pelas chaves e valores que são pedidas
# com isso, em uma lista vazia, adicono um dicionário com as chaves e valores que são pedidas
import requests
import json

requisicao = requests.get("https://jsonplaceholder.typicode.com/users")
users = (requisicao.json())

newJson = []

for pessoa in users:
    dados = {
    "name": pessoa["name"],
    "username": pessoa["username"],
    "email": pessoa["email"],
    "street": pessoa["address"]["street"],
    "suite": pessoa["address"]["suite"],
    }

    newJson.append(dados)

jsonFormatado = json.dumps(newJson, indent=2)
print(jsonFormatado)

#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO

# Nesse exercicio, irei utilizar a metodologia FIFO para a saida dos itens, pois tanto essa quanto LIFO
# dizem a respoito da forma que um item sai e não como entra

# Solução:
# nesta lista os itens foram adicionados em ordem alfabetica, para seguir a metodologia FIFO
# vamos ir retirando a partir do primeiro item adicionado "a"

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(lista)):
    x = lista.pop(0)
    print(x)

#11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO

# Nesse exercicio, irei utilizar a metodologia LIFO para a saida dos itens, pois tanto essa quanto FIFO
# dizem a respoito da forma que um item sai e não como entra

# Solução:
# nesta lista os itens foram adicionados em ordem alfabetica, para seguir a metodologia FIFO
# vamos ir retirando a partir do último item adicionado "z"

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(lista)):
    x = lista.pop()
    print(x)

#DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta

# Solução: Seguindo o comando do desafio, criei uma classe "Conta" que representa a conta de cada cliente
# Onde cada uma tem um id único que auto incrementa a cada conta nova
# e como comandos básicos de uma conta bancaria, essa tem: saque, depósito e ver o saldo da conta

class Conta:
  id = 1

  def __init__(self, nome, cpf):
    self.id = Conta.id
    Conta.id += 1
    self.nome = nome
    self.cpf = cpf
    self.__saldo = 0

  def saque(self, valor):
    if valor > 0 and valor <= self.__saldo:
      self.__saldo -= valor
      print(f"Saque de R${valor: .2f} realizado com sucesso!")
    else:
      print(f"Saque de R${valor: .2f} não pode ser realizado, pois seu saldo é insuficiente.")

  def deposito(self, valor):
    if valor > 0:
      self.__saldo += valor
      print(f"Depósito de R${valor: .2f} realizado com sucesso!")
    else:
      print(f"Valor do depósito precisa ser maior que R$00,00.")

  def ver_saldo(self):
    print(f"Seu salde é de R${self.__saldo: .2f}")








