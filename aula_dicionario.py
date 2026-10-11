def debug(*args):
    print(args)

N = int(input())

for _ in range(N):
    precos = {}
    
    M = int(input())
    
    for _ in range(M):
        entrada = input().split()
        
        nome = entrada[0]
        preco = float(entrada[1])
        
        precos[nome] = preco
        
    quantidades = {}
    
    P = int(input())
        
    for _ in range(P):
        entrada = input().split()
                
        nome = entrada[0]
        quantidade = int(entrada[1])
                
        quantidades[nome] = quantidade
    
    # como calculamos o preco
    soma = 0
    # quantidades, precos
    for nome in quantidades.keys():
        soma += quantidades[nome] * precos[nome]
    
    print(f"R$ {soma:.2f}")   
    