dicionario = {}

alfabeto = "a b c d e f g h i j k l m n o p q r s t u v x z".split()

tamanho_alfabeto = len(alfabeto)

vogais = {"a", "e", "i", "o", "u"}

for i in range(tamanho_alfabeto):
    letra = alfabeto[i]
    
    dicionario[letra] = {
        "esq": [],
        "dir": []
    }
    
    aux_esquerda = i - 1
    for _ in range(3):
        if aux_esquerda >= 0:
            dicionario[letra]["esq"].append(alfabeto[aux_esquerda])
        aux_esquerda -= 1
  
    
    aux_direita = i + 1
    for _ in range(3):
        if (aux_direita < tamanho_alfabeto):
            dicionario[letra]["dir"].append(alfabeto[aux_direita])
        
        aux_direita += 1

entrada = input()

resposta = []

for i in range(len(entrada)):
    letra_atual = entrada[i]
    
    if letra_atual in vogais:
        resposta.append(letra_atual)
        continue
    
    
    # Regra 1
    resposta.append(letra_atual)
    
    #Regra 2
    
    # percorrer a esquerda
    lista_esq = dicionario[letra_atual]["esq"]
    
    vogal_esq = ""
    dist_esq = 0
    for i in range(len(lista_esq)):
        le = lista_esq[i] 
        dist_esq += 1
        
        if le in vogais:
            vogal_esq = le
            break
        
    # percorrer a direita e no final pegar a vogal mais proxima
    lista_dir = dicionario[letra_atual]["dir"]
    
    vogal_dir = ""
    dist_dir = 0
    
    for i in range(len(lista_dir)):
        le = lista_dir[i] 
        dist_dir += 1
        
        if le in vogais:
            vogal_dir = le
            break
        
    if dist_esq < dist_dir and vogal_esq != "":
        resposta.append(vogal_esq)
    elif dist_esq > dist_dir and vogal_dir != "":
        resposta.append(vogal_dir)
    else:
        resposta.append(vogal_esq)
    
    # Regra 3
    lista_dir = dicionario[letra_atual]["dir"]
    
    if (len(lista_dir) == 0):
        resposta.append(letra_atual)
    else:
        
        for i in range(len(lista_dir)):
            le = lista_dir[i]
            
            if le not in vogais:
                resposta.append(le)
                break

r = "".join(resposta)
            
print(r)
    

