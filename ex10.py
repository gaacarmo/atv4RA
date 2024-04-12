lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
numRep = 0
numFrequente = 0

for i in lista:
    if lista.count(i) > numFrequente:
        numFrequente += 1
        numRep = i
print(f"dada a lista {lista}:\no numero {numRep} se repete mais vezes")