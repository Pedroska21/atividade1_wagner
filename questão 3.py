lista_vogal = ["a","e","i","o","u"]

letra = str(input("digite a letra desejada:")[:1])

if letra in lista_vogal:
    print ("a letra", letra, "é uma vogal")
else:
    print ("a letra", letra, "é uma consoante")