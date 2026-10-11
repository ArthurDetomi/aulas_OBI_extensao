entrada = input().split()
# li as entradas
N = int(entrada[0])
M = int(entrada[1])
P = int(entrada[2])
# Recebi e montei a matriz
matriz = []
for j in range(N):
    linha = input().split()
    
    for j in range(M):
        linha[j] = int(linha[j])
    
    matriz.append(linha)
    
# Lógica do jogo
soma_enzo = 0
soma_lobo = 0

for i in range(P):
    jogadas = input().split()
    
    linha = int(jogadas[0]) - 1
    coluna = int(jogadas[1]) - 1
        
    soma_coluna = 0
    for j in range(M):
        soma_coluna += matriz[linha][j]
        matriz[linha][j] = 0
    
    soma_linha = 0
    for j in range(N):
        soma_linha += matriz[j][coluna]
        matriz[j][coluna] = 0
        
    soma_total = soma_linha + soma_coluna
    
    if i % 2 == 0:
        soma_enzo += soma_total
    else:
        soma_lobo += soma_total

if soma_enzo > soma_lobo:
    print("Enzo")
elif soma_lobo > soma_enzo:
    print("Lobo")
else:
    print("Empate")
    


    