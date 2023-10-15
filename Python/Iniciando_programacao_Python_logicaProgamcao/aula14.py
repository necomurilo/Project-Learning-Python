a = 'AAA'
b = 'B'
c = 1.1
string = 'a={nome1} a={nome1} b={nome2} c={nome3:.2f} '
formato = string.format(nome1=a, nome2=b, nome3=c)
# Confuso
print(formato) 
print('"Já sei!"')


# tudo em python é um objeto


nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos' # Começa sempre do zero
print(formato.format(nome, idade))

nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))

nome = "Luiz"
idade = 23
formato = f'{nome} tem {idade:.2f} anos'

numero_1 = 10
numero_2 = 20
resultado = numero_1 * numero_2
print(resultado)