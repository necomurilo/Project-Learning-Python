
# Fatiamento de strings
#  012345678
#  Olá mundo
# -987654321

# Fatiamento [i:f:p] (< quer dizer inicio e fim e P pular casas) [::]
# i = inicio
# f = fim
# p = pular ou selecionar conforme o valor (selecionar de 3 em 3 letras)
# Obs.: a função len retorna a qtd 
# de caracteres da str

variavel = 'Olá mundo'
print(variavel[::1])
print(variavel[0:9:2])
print(variavel[-1:-10:-1])