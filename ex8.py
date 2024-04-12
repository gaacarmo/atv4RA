num = int(input("Digite um numero para descobrir os divisores: "))
divisores = []

for i in range(1, num + 1):
    if num % i == 0:
        divisores.append(i)

print(f"Os divisores do numero {num} são: {divisores}")

if len(divisores) == 2:
    print(f"{num} é primo!")

        
    