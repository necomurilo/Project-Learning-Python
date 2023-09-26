"""
Repetições
while (enquanto) for verdadeiro
Executa uma ação enquanto uma condição for verdadeira

LOOP INFINITO - quando um código nao tem fim
"""

# Cuidado, código com loop infinito 
condicao = True

while condicao:
    nome= input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
#para encerrar, ele busca o while mais próximo
    if nome == 'sair':
        break

print('Acabou')