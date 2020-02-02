a = int(input("Digite um numero a ser multiplicado: "))
b = int(input("Digite outro numero: "))
x=0
z=1
print(a, "X", b, "=", (a*b))
while x<b:
    print (a, end= ' ')
    x+=1
    if z < b:
        print("+", end = ' ')
        z+=1

print (" = ", end = ' ')
x=0
z=1
while x<a:
    print (b, end= ' ')
    x+=1
    if z < a:
        print("+", end = ' ')
        z+=1

    
