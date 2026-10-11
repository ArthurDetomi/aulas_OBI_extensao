def debug(*args):
    pass
    #print(*args)

def somaDosNValores(inicial, n):
    a1 = inicial
    an = inicial + (n - 1)

    return ((a1 + an) * n) // 2
    
def buscaResposta(min, max, L, A):
    inicio = min
    fim = max
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
            
        somaAteN = somaDosNValores(A, meio)
        
        an = A + (meio - 1)
        
        debug(f"inicio={inicio}, fim={fim}, meio={meio}, somaAteN={somaAteN}, an={an}")
        
        # encontrei a resposta correta se
        if somaAteN == L or (somaAteN > L and somaAteN - an < L) or (inicio == fim):
            return meio

        #caso venha para cá eu ainda não encontrei a resposta
        if somaAteN < L:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    # caso que nunca ocorre
    return 1
            

# Solução trivial com timelimit
def main():
    P = int(input())

    for _ in range(P):
        entrada = input().split()
        
        L = int(entrada[0])
        A = int(entrada[1])
        B = int(entrada[2])
        
        debug(f"L={L}, A={A}, B={B}\n")
        
        min_rodadas = 1
        max_rodadas = B - A + 1

        
        resposta = buscaResposta(min_rodadas, max_rodadas, L, A)
        
        print(resposta)
            
if __name__ == "__main__":
    main()
    