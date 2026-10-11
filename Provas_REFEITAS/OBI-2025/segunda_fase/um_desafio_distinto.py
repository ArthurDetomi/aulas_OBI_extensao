# Solução trivial com timelimit
def main():
    P = int(input())

    for _ in range(P):
        entrada = input().split()
        
        L = int(entrada[0])
        A_MIN = int(entrada[1])
        B_MAX = int(entrada[2])
        
        somaCaixa = 0
        rodadas = 0
        
        for x in range(A_MIN, B_MAX + 1):
            somaCaixa += x
            
            rodadas += 1
            
            if somaCaixa >= L:
                break    
        
        print(rodadas)
        
if __name__ == "__main__":
    main()
        