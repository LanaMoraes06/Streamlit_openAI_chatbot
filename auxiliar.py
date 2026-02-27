# lista
lista_nova = []
nomes = ["Gusthavo", "Lana", "Ana", "Micelle"]
print(nomes[0])

nomes.append("Gusthavo")
print(nomes)

#dicionario

idades = {"Gusthavo": 18, "Lana": 19, "Ana": 20, "Micelle": 21} #Pega a informação do dicionário -> dicionario[chave]
print(idades["Gusthavo"])

#Role = quem é o usuário

mensagem1 = {"role": "IA", "content": "Bora aprender python"}
mensagem2 = {"role": "user", "content": "Bora sim, bora aprender"}
mensagem3 = {"role": "IA", "content": "Entao vamos começar a aula"}

lista_mensagens = [mensagem1, mensagem2, mensagem3]
print(lista_mensagens)

nova_mensagem = {"role": "user", "content": "vamo que vamo"}
lista_mensagens.append(nova_mensagem)
print(lista_mensagens)

