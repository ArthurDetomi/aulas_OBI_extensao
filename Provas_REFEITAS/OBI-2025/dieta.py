N, M = list(map(int, input().split()))

for _ in range(N):
    P, G, C = list(map(int, input().split()))
    
    M -= (P * 4 + G * 9 + C * 4)
    
print(M)