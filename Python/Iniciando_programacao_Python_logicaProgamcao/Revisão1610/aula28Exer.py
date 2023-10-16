nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

if nome and idade:
    print(f'seu nome é: {nome}')
    print(f'Seu nome invertido é:  {nome[::-1]}')

    if ' ' in nome: #conta os espaços no nome
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')  

    print(f'seu nome tem: {len(nome)} letras') #len conta quantas letras tem

    print(f'A primeira letra do seu nome é: {nome[0]}')

    print(f'A ultima letra do seu nome é: {nome[-1]}') # mostra a ultima letra do nome.



else:
    print("Desculpe, você dixou campos vazios.")