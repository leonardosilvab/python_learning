#Exercício 4.2 - Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h , exiba
# a mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80km/h

a = int (input("Qual a velocidade: "))
if a>80:
    print("Multado")
    multa = (a-80)*5
    print("A multa sera de: ", multa)
else: 
    print("nao multado")
