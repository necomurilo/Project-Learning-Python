hora = float(input('Digite a hora: '))

if hora <= 11:
    print("Bom dia!")
elif hora >= 12 and hora <= 17:
    print("Boa tarde!") 
elif hora >= 18 and hora <= 23:
    print("Boa noite!")
else:
    print("hora inválida!")