idade = int(input("insira sua idade:\n"))
if idade < 0:
    print("impossivel!\n não precisa se alistar.")
if idade < 18:
    print("não precisa se alistar.")
else:
    if idade > 18 and (idade < 65):
        print("Não esqueça de votar na próxima eleição.")
    if idade > 65:
        print("Vá descansar.")
    if idade == 18 or idade == 65:
        print("eita!")