N = int(input())

respostas = input().split()

for linha in range(N):
    respostas[linha] = int(respostas[linha])
    
maior = respostas[0]
for linha in range(N):
    if respostas[linha] > maior:
        maior = respostas[linha]
        
qtdLinhas = maior
qtdColunas = N

matriz = []

for linha in range(qtdLinhas):
    lista = []
    
    for coluna in range(qtdColunas):
        lista.append(0)
        
    matriz.append(lista)

for coluna_fixa in range(qtdColunas):
    
    qtdAPreencher = respostas[coluna_fixa]
    
    linhaInicial = qtdLinhas - 1
    
    for coluna in range(qtdAPreencher):
        matriz[linhaInicial][coluna_fixa] = 1
        
        linhaInicial = linhaInicial - 1


for linha in range(qtdLinhas):
    for coluna in range(qtdColunas):
        print(matriz[linha][coluna], end=" ")
    print() # só quebra a linha
