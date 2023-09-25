nome = input("Por favor insira seu nome: ")
quantidade_letras = len(nome)
print(f'seu nome tem: {len(nome)} letras')

if quantidade_letras <= 4:
    print('Seu nome é curto')
elif quantidade_letras >= 5 and quantidade_letras <= 6:
    print("Seu nome tem um tamanho normal")
else:
    print("Seu nome é muito grande!")