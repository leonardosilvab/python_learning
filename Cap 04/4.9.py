valor = float(input("Digite o valor da casa: "))
salario = int(input("Digite o salario: "))
anos = int(input("Digite a quantidade de anos a pagar: "))

meses = anos*12
prestacao = valor/meses

if prestacao > (salario*0.30):#0.30 == 30% do salario
    print("emprestimo nao aprovado")
else:
    print ("Emprestimo aprovado!")
    
