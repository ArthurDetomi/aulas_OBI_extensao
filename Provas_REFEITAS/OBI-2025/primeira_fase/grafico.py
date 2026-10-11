N = int(input())
respostas = list(map(int, input().split()))

maior = max(respostas)

# cria matriz
mat = []
for i in range(maior):
    mat.append([0] * N)

for i in range(len(respostas)):
    nota_atual = respostas[i]
    
    pos_aux = maior - 1
    
    for j in range(nota_atual):
        mat[pos_aux][i] = 1
        pos_aux -= 1        

for i in range(maior):
    for j in range(N):
        print(mat[i][j], end=" ")
    print()
    
