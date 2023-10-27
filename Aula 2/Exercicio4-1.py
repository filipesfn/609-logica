letra = str(input("Digite uma letra")).lower()


letra = str(input("Digite uma letra"))

if letra in "aeiou":
    print("Essa {letra} é uma vogal")
elif letra in "bcdfghjklmnpqrstvwxyz":
    print("Essa letra é uma consoante")
else:
    print("Caracter invalido")
    
    print("Essa {letra} é uma consoante")

    if letra in 'aeiou':
        print("é uma vogal")
    elif letra in 'bcdfghjklmnpqrstuvwxyz':
        print("é uma consoante")
    else:
        print("Caracter inválido")
