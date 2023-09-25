"""
Flag (Bandeira) - Marca um local
None = Não valor
is e is not = e ou não é (tipo, valor, identidade)
id = identidade
"""


"""
Assunto mais avançado, isso foi apenas uma introdução.
v1 e v2 tem o mesmo valor, qualquer modificaçao torna isso falso
v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))
"""


condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

# is é a mesma coisa de ==
#print(passou_no_if, passou_no_if is None)
#print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')