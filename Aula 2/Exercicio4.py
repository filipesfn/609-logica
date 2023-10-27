letra = str(input("Digite uma letra")).lower()


letra = str(input("Digite uma letra"))

if letra == 'a' or letra == 'e' or letra =='i' or letra == 'o' or letra == 'u':
    print("Essa {letra} é uma vogal")
else:
    print("Essa {letra} é uma consoante")

    if letra in 'aeiou':
        print("é uma vogal")
    elif letra in 'bcdfghjklmnpqrstuvwxyz':
        print("é uma consoante")
    else:
        print("Caracter inválido")

