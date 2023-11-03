nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
nota4 = float(input("Digite a quarta nota:"))

if nota1 >= nota2 and nota1 >= nota3 and nota1 >= nota4:
    print(f"a maior nota é a {nota1}")
if nota2 >= nota1 and nota2 >= nota3 and nota2 >= nota4:
    print(f"a maior nota é a {nota2}")
if nota3 >= nota1 and nota3 >= nota2 and nota3 >= nota4:
    print(f"a maior nota é a {nota3}")
if nota4 >= nota1 and nota1 >= nota2 and nota4 >= nota3:
    print(f"a maior nota é a {nota4}")
