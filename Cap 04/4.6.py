distancia = int(input("Digite a distancia a ser percorrida: "))

if distancia <= 200:
    valor = distancia*0.5
else:
    valor = distancia*0.45

print("R$: %5.2f." %valor)
