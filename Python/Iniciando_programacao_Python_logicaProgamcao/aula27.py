"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] (< quer dizer inicio e fim e P pular casas) [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::1])
print(variavel[0:9:2])
print(variavel[-1:-10:-1])