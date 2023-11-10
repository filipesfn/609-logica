cliente = []
soma = 0 

while True:
   cliente_nome = str(input("Digite o nome do cliente: "))
   cliente_telefone = int(input("Digite o numero do cliente: "))
   cliente_endereço = str(input("Digite seu endereço: "))
   cliente_dados = (cliente_nome, cliente_telefone, cliente_endereço)
   cliente.append(cliente_dados)

   print(cliente)


