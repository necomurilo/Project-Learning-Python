# Variáveis são usadas para salvar algo na memória do computador
# PEP8: inicie variáveis com letras minúsculas, pode usar: números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um nome (variavel)
# Uso: nome_variavel = expressão

nome_completo = 'Murilo Lima Neco'
soma_dois_mais_dois = 0 + 1
print(nome_completo, soma_dois_mais_dois)

int_um = bool('1') # cuidado é um bool, mas esta escrito como inteiro por não ter sido alterado no momento da correção. (não cometer esse tipo de erro)
print(int_um, type(int_um))


nome = "Murilo"
idade = 28
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)