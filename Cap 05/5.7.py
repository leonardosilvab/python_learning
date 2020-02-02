inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))

x=1

while(x<=fim):
    print(inicio," X ",x, "= ",(inicio*x) )
    print (f"{inicio} X {x} = {(inicio*x)}")
    x+=1
