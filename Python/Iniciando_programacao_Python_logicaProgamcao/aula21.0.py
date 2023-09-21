# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# Se qualquer valor for considera falso, a expressão inteira será avaliada naquele valor
# são considerados falsy (que vc já viu)
# 0 0.0 '' False (zero, zero.zero, string vazia e False)
# também existe o tipo Nome que é usado para representar um não valor



entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')


senha_permitida = '123456'
# if condicao: 
# ... só é exucatado quando tudo for True:
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

#Flasy não é necessáriamente FALSO