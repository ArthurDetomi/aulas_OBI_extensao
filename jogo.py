import random # importar biblioteca

MIN = 1
MAX = 20
MAX_TENTATIVAS = 5


numeroAleatorio = random.randint(MIN, MAX)


tentativas = MAX_TENTATIVAS

jogoTerminou = False

while True:
    if jogoTerminou:
        resposta = input("Deseja jogar novamente? sim/nao")
        
        if resposta == "sim":
            tentativas = MAX_TENTATIVAS
            jogoTerminou = False
        else:
            print("Até mais! :)")
            break
        
    valorDigitado = int(input(f"Digite um numero entre {MIN} e {MAX}:"))

    if valorDigitado > numeroAleatorio:
        tentativas -= 1
        
        if tentativas == 0:
            print("Você perdeu")
            jogoTerminou = True
            continue
            
        
        print(f"O numéro é menor restam {tentativas} tentativas")
    elif valorDigitado < numeroAleatorio:
        tentativas -= 1
        
        if tentativas == 0:
            print("Você perdeu")
            jogoTerminou = True
            continue
        
        print(f"O numéro é maior restam {tentativas} tentativas")
    else:
        # Nesse caso aqui é igual
        print(f"Você ganhou usando {tentativas} tentativas")
        jogoTerminou = True


        
        

