while True:
    nome = str(input("Digite um nome: "))
    senha = str(input("Digite uma senha: "))

    if nome == senha:
        print("Escolha uma nova senha")

    else:
        print("Senha válida")
        break

