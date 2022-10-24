import random
list =[]

for x in range(30):
    x = random.randint(1, 10)
    list.append(x)

numero = int(input("Digite um numero de 1 a 30: "))
contador = 0
for x in list:
    if x in list:
        if x == numero:
            contador +=1

print(f"REPETIÇÃO DE NUMEROS{contador}")
print(list)