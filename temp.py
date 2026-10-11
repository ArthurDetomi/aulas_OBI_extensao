def criaCopiaMatriz(matriz, n):
    matrizNova = []
    
    for i in range(n):
        linhas = []
        for j in range(n):
            linhas.append(matriz[i][j])
        matrizNova.append(linhas)
        
    return matrizNova

n = 5
matriz1 = []

for i in range(n):
    linhas = []
    for j in range(n):
        linhas.append(j)
    matriz1.append(linhas)

for i in range(n):
    print(matriz1[i])
    
matriz2 = criaCopiaMatriz(matriz1, n)

matriz1[0][3] = 99


print("Matriz 1")
for i in range(n):
    print(matriz1[i])

print("Matriz 2")
for i in range(n):
    print(matriz2[i])



    
    