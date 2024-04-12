idade = 0
lista = []
for i in range(0,5):
    lista.append(int(input("Digite sua idade: ")))
    i+=1
soma = sum(lista)
media = (soma/i)
print(f"A média das idades foi de {media}")
