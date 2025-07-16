
#imc - indice de massa corporea

#imc = peso / altura ** 2
#ou
#imc = peso / (altura * altura)
#ENTRADA
nome='lucas'
altura= 1.71
peso= 80
#PROCESSAMENTO
imc= peso/ altura**2 

print(nome, 'tem', altura, 'pesa', peso , 'seu imc é =>', imc)
#s-strings
print(f'{nome} tem {altura} pesa {peso} seu imc é {imc:.2f}' )
