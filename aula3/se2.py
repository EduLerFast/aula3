entrada= input('você quer [entrar ou sair]')
entrada= entrada.lower()
print (entrada)
if entrada == 'entrar':
    print('seja bem vindo, entrou no sistema')

elif entrada == 'sair':
    print('até mais....')
else:
    print('voce nao digitou nem entrar e nem sair')
