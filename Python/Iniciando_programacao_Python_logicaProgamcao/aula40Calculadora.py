""" Calculadora com while """
# while True:
#     sair = input('Quer sair? [s]im: ')
#     sair = sair.lower() # converte para minusculo
#     sair = sair.startswith('s')  # checa se começa com a letra s
#     # termina com uma letra .endswith
#     print(sair)

#RESUMO do código acima

while True:
    print('nummmmm')
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break