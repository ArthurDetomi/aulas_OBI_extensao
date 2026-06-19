entrada = input().split()

N = int(entrada[0])
K = int(entrada[1])

notas = input().split()
for i in range(N):
    notas[i] = int(notas[i])
    
notas.sort()

posNotaCorte =  N - K

notaCorte = notas[posNotaCorte]

print(notaCorte)