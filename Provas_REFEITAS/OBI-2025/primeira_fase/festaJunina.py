distancias = []

for i in range(3):
    num = int(input())
    
    distancias.append(num)
    
distancias.sort()    
    
response = (distancias[2] - distancias[0]) + (distancias[1] - distancias[0]) + (distancias[2] - distancias[1])

print(response) 
    
    