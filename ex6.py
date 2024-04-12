intervalo = [10,11,12,13,14,15,16,17,18,19,20]
countin = 0
countout = 0
for i in range(1,11):
    num = int(input(f"Digite aqui o {i} numero: "))
    
    if num >= 10 and num <= 20:
        countin += 1
    else:
        countout += 1
print(f"Você digitou {countin} numeros dentro do intervalo e {countout} numeros fora")
