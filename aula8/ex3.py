n1 = int(input("Digite um número"))
n2 = int(input("Digite outro número"))
r = input("Qual operação você deseja fazer?")
if r == "+":
    s = n1+n2
    print(s)
elif r == "-":
    s = n1-n2
    print(s) 
elif r == "*":
    s = n1*n2 
    print(s) 
elif r == "/":
    s = n1/n2
    print(s)
elif r == "**":
    s = n1**n2
    print(s)
else:
        print("Negado!")