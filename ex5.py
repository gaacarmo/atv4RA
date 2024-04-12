par = 0
impar = 0

for i in range(1,11):
    num = int(input(f"Digite aqui o {i} numero: "))
    i += 1
    if num %2 == 0:
        par += 1
    else:
        impar += 1
print(f"|Você digitou {par} numeros pares| \n|Você digitou {impar} numeros impares|")