"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
 que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços
   em 3 situações: • comprar apenas latas de 18 litros; • comprar apenas galões de 3,6 litros; • misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e
     sempre arredonde os valores para cima, isto é, considere latas cheias."""



tamanho= float (input('qual o tamanho da area?:')) #tamanho base 16
tamanho_ao_quadrado=tamanho**2
print (f'{tamanho}²={tamanho**2}')
#256 metros....
tintapormetro=tamanho_ao_quadrado /3 
#print (tintapormetro//18)

if tamanho_ao_quadrado<= 1:
  print ('compre',(tintapormetro//18)+1 ,'lata de tinta de 18 litros') 

elif tamanho_ao_quadrado  <= 100    > 1:
 print ('compre',tintapormetro//18 ,'lata de tinta de 18 litros')


elif tamanho_ao_quadrado >= 101:
 print ('compre',tintapormetro//18 ,'latas de tinta de 18 litros')


tamanho_ao_quadrado=tamanho**2
tintapormetro=tamanho_ao_quadrado /6
if tamanho_ao_quadrado<= 1:
  print ('compre', (tintapormetro//3,6 +1) ,'lata de tinta de 3,6 litros') 

elif tamanho_ao_quadrado  <= 100    > 1:
 print ('compre',tintapormetro//3,6 ,'lata de tinta de 3,6 litros')


elif tamanho_ao_quadrado >= 101:
 print ('compre',tintapormetro//3,6 ,'latas de tinta de 3,6 litros')


 preco=(tintapormetro//18 )*80
if preco<= 1:
 print(f'irá custar R${preco+80} em latas de 18 litros')

else:
 print(f'irá custar R${preco} em latas de 18 litros')


preco2=(tintapormetro//3.6 )*25


print(f'irá custar R${preco2}')

print(f'irá custar R${preco2 + 25}')



