#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. A = π * r²
pi= float(3.141592653589793238462643383279502884197169)
raio= float (input ('Coloque o raio do circulo:'))
area= pi * raio ** 2
print (f'A area do circulo é: {area:.2f}')