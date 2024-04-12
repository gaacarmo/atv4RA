soma = 0
count = 0
num = 0

while count < 50:
    if num % 2 == 0:   
        soma += num
        count += 1
    num += 1

print(f"A soma dos 50 primeiros números pares é: {soma}")

