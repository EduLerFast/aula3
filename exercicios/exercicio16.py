#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a 
# cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
#  quantidades de latas de tinta a serem compradas e o preço total.

# nao sei se ta correto

tamanho= float (input('qual o tamanho da area?:')) #tamanho base 16
tamanho_ao_quadrado=tamanho**2
print (f'{tamanho}²={tamanho**2}')
#256 metros....
tintapormetro=tamanho_ao_quadrado /3 

if tamanho_ao_quadrado<= 1:
  print ('compre',(tintapormetro//18)+1 ,'lata de tinta') 

elif tamanho_ao_quadrado  <= 100    > 1:
 print ('compre',tintapormetro//18 ,'lata de tinta')


elif tamanho_ao_quadrado >= 101:
 print ('compre',tintapormetro//18 ,'latas de tinta')




preco=(tintapormetro//18 )*80
if preco< 1:
 print(f'irá custar R${preco+80}')

else:
 print(f'irá custar R${preco}')

