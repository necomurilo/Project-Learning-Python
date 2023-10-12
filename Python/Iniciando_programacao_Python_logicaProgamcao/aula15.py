# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')


numero_1 =input('Digite um número: ')
numero_2 = input('Digite outro número: ')
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)
# Cuiado, pois se colocar numero_1 = int(input('Digite um numero')
# gera uma quebra de sistema e pode gerar muitos problemas futuros, impedindo o dev de encontrar o que levou o sistema quebrar.

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')