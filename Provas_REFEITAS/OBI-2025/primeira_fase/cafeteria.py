A = int(input())
B = int(input())
C = int(input())
D = int(input())

faltante = 0

possivel = False

mult = 1


while True:
    faltante = C - (mult * D) 
        
    if faltante >= A and faltante <= B:
        possivel = True
        break
    
    if faltante < A:
        break
    
    mult += 1
    
if possivel:
    print("S")
else:
    print("N")
    