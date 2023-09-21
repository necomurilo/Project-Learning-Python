print(True and False and True)
# isso é uma avaliação de curto circuito
print(True and 0 and True)
# pode ser que ele  retorne o valor da condição
print(bool(0.0))


# O 0 (zero) de 0 and 1 avalia como falsy. O corpo do if não será executado.
#if 0 and 1:
#    print(True and 1)
 

if 1 and 1:
    print(True and 1 and False)