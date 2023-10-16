# 1 if / elif       / else
# se  /  se não se / se não

# ... ou pass (quando a pessoa não quer escrever o código)

condicao = False # True ou False

if condicao:
    print('Este e o código do if')
else: 
    print('contrario de if') #else do primeiro if

print('Fora do if')


if 10 == 10: 
    print('Outro if')



# if / elif      / else
# se / se não se / se não

condicao1 = False # ele vai executar paenas a primeira True, o resto ele vai pular.
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')

