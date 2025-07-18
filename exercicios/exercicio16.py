#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a 
# cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
#  quantidades de latas de tinta a serem compradas e o preço total.

tamanho= float (input('qual o tamanho da area?:'))**2 
tintapormetro=0.03 * tamanho
coberturadatinta=3 **2
lata= 18
quantidadelata=tamanho/coberturadatinta
print (tamanho/lata) #quantidade de litros gasto
