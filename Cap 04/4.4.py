#Exercício 4.3 -  Escreva um programa que leia três números e que imprima o maior e o menor.

a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))

if a>b and a>c:
    print (a)
if b>a and b>c:
    print (b)
if c>a and c>b:
    print (c)
