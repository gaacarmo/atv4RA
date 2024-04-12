listaDeNumeros = []

for i in range (1,11):
    listaDeNumeros.append(int(input(f"Digite o {i} valor inteiro e positivo: ")))
listaDeNumeros.sort()
print(f"Lista em ordem crescente: {listaDeNumeros}")