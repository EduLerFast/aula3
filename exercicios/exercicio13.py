#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: • Para homens: (72.7h) - 58 • Para mulheres: (62.1h) - 44.7
altura= float (input ('Coloque sua altura:'))
homem_mulher=(input ('voce é homem ou mulher:'))

if homem_mulher== ('homem'):
 print (f'seu peso ideal é {72.7 * altura - 58:.2f}')

elif homem_mulher== ('mulher'):
 print (f'seu peso ideal é {62.1 * altura - 44.7:.2f}')