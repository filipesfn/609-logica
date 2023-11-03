# for numero in range(1,11):
#     print(numero)

# for numero in range (2, 21, 2):
#     print(numero)


# for numero in range (1, 20, 2):
#     print (numero)

# soma = 0

# for numero in range (1,101):
#     soma = soma + numero
# print("Soma total", soma)


# soma = 0
# for i in range(1,7):
#     numero = int(input(f"Digite o {i}º número: "))
#     soma = soma + numero

# media = soma / 6

# print(f"A média do números foi {media} ")



# nome = str(input("Digite seu nome: "))
# for letra in nome:
#     print (letra)



# palavra = str(input("Digite uma palavra: "))
# contador_vogais = 0

# for letra in palavra:
#     if letra.lower() in "aeiou":
#         contador_vogais = contador_vogais + 1


# print(f"A palavra '{palavra}' possui {contador_vogais} vogais")



palavra = str(input("Digite uma palavra: "))
contador_consoantes = 0

for letra in palavra:
    if letra.lower() in "bcdfghjklmnpqrstvxywz":
        contador_consoantes = contador_consoantes + 1


print(f"A palavra '{palavra}' possui {contador_consoantes} vogais")