#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
farenheit= float (input ('coloque os graus farenheit para converter:'))
celsius= (5 * (farenheit - 32) / 9)
print (f'o resultado é : {celsius:.2f}')