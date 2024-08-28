print ("responda as seguintes questões com sim ou não")
pergunta1 = str (input("Telefonou para a vitima?"))
pergunta2 = str (input("Esteve no local do crime?"))
pergunta3 = str (input("Mora perto da vitima?"))
pergunta4 = str (input("Devia para a vitima?"))
pergunta5 = str (input("Já trabalhou com a vitima?"))
sim = 0
if (pergunta1 == "sim"):
    sim +=1
if (pergunta2 == "sim"):
    sim +=1
if (pergunta3 == "sim"):
    sim+=1
if (pergunta4 == "sim"):
    sim+=1
if (pergunta5 == "sim"):
    sim+=1
if sim <=1:
    print ("Inocente")
elif sim ==2:
    print("Suspeita")
elif sim ==3 or sim ==4:
    print ("Cúmplice")
elif sim >4:
    print ("Assassino")
