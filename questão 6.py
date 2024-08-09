turno = str (input("em qual turno você estuda, insira M-Matutino, V-Vespertino, N-Noturno: ")[:1])

if (turno == "m") or (turno == "M"):
    print("bom dia")
elif (turno == "v") or (turno == "V"):
    print("boa tarde")
elif (turno == "n") or (turno == "N"):
    print("boa noite")
else:
    print("Valor invalido!")