nota1 = float (input("digite a primeira nota: "))
nota2 = float (input("digite a segunda nota: "))
resultado = nota1 + nota2

if (resultado / 2 >= 7 and resultado < 10):
    print ("aprovado")
elif (resultado / 2== 10):
    print ('aprovado com dinstinção')
else:
    print ('reprovado')
