massa = float(input("Qual sua altura atual?"))
altura = float(input("Qual sua altura?"))
imc = (massa/altura**2)

if imc < 18.5:
    print("Abaixo do peso!")
elif 18.5 <=imc<24.9:
    print("Peso na media!")
elif 25<=imc<29.9:
    print("Acima da media!")
elif 30<=imc<34.9:
    print("Obeso!")
else:
    print("Você está muito a cima da media, obesidade 3° grau!")
