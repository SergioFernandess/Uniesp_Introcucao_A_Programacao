from math import pow,sqrt

x1 = int(input("Digite um número"))
y1 = int(input("Digite um número"))
x2 = int(input("Digite um número"))
y2 = int(input("Digite um número"))

d = sqrt(pow((x1-x2),2)+ pow((y1-y2),2))
print(f"{d:2f}")
