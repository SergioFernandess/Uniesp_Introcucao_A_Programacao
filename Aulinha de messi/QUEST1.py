print("Digitr 10 Clubes")
clubes = []

for i in range(1,11):
    clube = input("Digite um clube:")
    clubes.append(clube)

clube_os_escolhidos = input("Escolha um clube:")
if clube_os_escolhidos in clubes:
    print("LOCALIZADO !")
else:
    print("NÃO LOCALIZADO !")