#       012345678910
nome = 'Murilo Neco' # Interáveis
#       109876543210
#tamanho_nome = len(nome)
indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
novo_nome += '*'
print(novo_nome)





# qtd_linhas = 5
# qtd_colunas = 5

# linha = 1
# while linha <= qtd_linhas:
#     coluna = 1
#     while coluna <= qtd_colunas:
#         print(f'{linha=} {coluna=}')
#         coluna += 1
#     linha += 1


# print('Acabou')