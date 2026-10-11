n = int(input())

# Aqui eu tenho as traduções de todas as linguas
traducoes = {}

for i in range(n):
   lingua = input()
   mensagem = input()
   
   traducoes[lingua] = mensagem

m = int(input())

# Uma lista com todas crianças
# Dentro dessa lista tem um dicionario com as informações
# (nome e lingua)
criancas = []

for i in range(m):
    nome = input()
    lingua = input()
    
    criancas.append({"nome": nome, "lingua": lingua})

# Código
# Tem que imprimir as etiquetas
# Desafio: Completar o código
for i in range(len(criancas)):
    nomeCrianca = criancas[i]["nome"]
    lingua = criancas[i]["lingua"]
    
    print(nomeCrianca)
    print(traducoes[lingua])
    print()

