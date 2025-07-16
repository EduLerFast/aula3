#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% 
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: • salário bruto. • quanto pagou ao INSS. • quanto pagou ao sindicato. 
# • o salário líquido. • calcule os descontos e o salário líquido, conforme a
#  tabela abaixo: Salário Bruto : R$ IR (11%) : R$ INSS (8%) : R$ Sindicato ( 5%) : R$ Salário Liquido : R$ Obs.: Salário Bruto - Descontos = Salário Líquido.

ganho_hora= float (input  ('quanto voce ganha por hora?:'))
horas_trabalho= float (input  ('quantas horas voce trabalha no mes?:'))
salariobruto=ganho_hora * horas_trabalho

#desconstos
salariodescontadoimpostoderenda=( 89 % salariobruto )
salariodescontadoinss= (92% salariobruto)
salariodescontadosindicato=(95% salariobruto)

salarioliquido= (salariobruto - salariodescontadoimpostoderenda - salariodescontadoinss - salariodescontadosindicato )

print (f' salario bruto: {salariobruto} R$ IR (11%) : R$ INSS (8%) R$ Sindicato (5%) :R$ Salario Liquido {salarioliquido} ')
