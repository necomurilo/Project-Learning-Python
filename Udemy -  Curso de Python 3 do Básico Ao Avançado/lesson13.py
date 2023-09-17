nome = 'Murilo Lima Neco'
altura = 1.96
peso = 102
imc = peso / (altura)**2


linha_1 = f'{nome} tem {altura:.2f} de altura'
#utilizar assim, pois é mais organizado
#:.2f = 2 casas decimais
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'




print(linha_1)
print(linha_2)
print(linha_3)
# print(nome,"tem", altura,'de altura','pesa', peso, 'quilos e seu IMC é', imc)