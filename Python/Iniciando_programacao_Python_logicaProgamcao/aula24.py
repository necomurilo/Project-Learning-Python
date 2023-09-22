# Operadores in e not in (estar entre e não estar entre)
# Strings são iteráveis
# 0 1 2 3 4 5 
# M u r i l o
#-6-5-4-3-2-1

nome = 'Murilo'
#print(nome[2])
#print(nome[-6])

#print('M' in nome)
#print(10 * '-')
#print('Mur' in nome)
#print(10 * '-')
#print('Muril' in nome)
#print(10 * '-')
#print('Mamaco' in nome)
#print(10 * '-')


nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em{nome}')
else:
    print(f'{encontrar} não está em {nome}')