def criarCopiaMatriz(matriz, N):
    newMatriz = []
    
    for i in range(N):
        linhas = []
        for j in range(N):
            linhas.append(matriz[i][j])
        newMatriz.append(linhas)
        
    return newMatriz

def obterQuantidadeVizinhosVivo(matriz, N, linha, coluna):
    posLinha  = linha - 1
    somaVizinhos = 0
    
    for _ in range(3):
        posColuna = coluna - 1
        
        for _ in range(3):
            if posLinha == linha and posColuna == coluna:
                posColuna += 1
                continue
            if posLinha < 0 or posLinha >= N or posColuna < 0 or posColuna >= N:
                posColuna += 1
                continue
            
            somaVizinhos += matriz[posLinha][posColuna]
            
            posColuna += 1
            
        posLinha += 1    
    
    return somaVizinhos
    

N, Q = list(map(lambda v : int(v), input().split()))

matriz = []

for i in range(N):
    linhasStr = input()

    linhasArr = []
        
    for j in range(N):
        linhasArr.append(int(linhasStr[j]))
    
    matriz.append(linhasArr)
    
for _ in range(Q):
    matrizEstadoAnterior = criarCopiaMatriz(matriz, N)
    
    for linha in range(N):
        for coluna in range(N):
            quantidadeVizinhos = obterQuantidadeVizinhosVivo(matrizEstadoAnterior, N, linha, coluna)
            
            celula = matriz[linha][coluna]
            
            # Se a celula é 0 ela ta morta
            if celula == 0:
                # Se uma célula morta possui exatamente três vizinhas vivas, ela vira uma célula viva;
                if quantidadeVizinhos == 3:
                    matriz[linha][coluna] = 1
            else: # se a celula ta viva faça:
                """
                Se uma célula viva possui menos que duas vizinhas vivas, ela morre;
                Se uma célula viva possui mais que três vizinhas vivas, ela morre.
                """
                if quantidadeVizinhos < 2 or quantidadeVizinhos > 3:
                    matriz[linha][coluna] = 0

for linha in range(N):
    for coluna in range(N):
        print(matriz[linha][coluna], end="")
    print()    