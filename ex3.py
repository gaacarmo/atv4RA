num = int(input("Digite um numero de 1 até 10: "))
for i in range(1,11):
    if num > 10:
        exit("numero maior que 10 não permitido")
    elif num < 1:
        exit("Numero menor que 1 não permitido")
    print(f"|{num} x {i} = {num * i}|")
