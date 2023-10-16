# Organizador de dados (print)

"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.2f
Conversion flags - !r !s !a 
__repr__ __str__
"""

variavel ='ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # direita
print(f'{variavel: <10}') # esquerda
print(f'{variavel: ^10}') # Centro
print(f'{-1000.0000000:,.2f}')
#print(f'{1000.0000000:+,.2f}')
#print(f'{1000.0000000:0>+10,.2f}')
#print(f'{1000.0000000:0=+10,.2f}')


print(f'O hexadecimal de 1234567 é {1234567:08X}') 
