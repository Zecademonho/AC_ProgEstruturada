#--baskara--
#pedir a b c ao user
print("Considerando que as raizes tem que ser reais e a diferente de 0")
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
#calcular baskara
x1= ((-b + (b**2 - 4 * a * c)**1/2)/ 2 * a)
x2= ((-b - (b**2 - 4 * a * c)**1/2)/ 2 * a)
print(x1, x2)


#--ano bissexto--
#pedir o ano ao user
ano=int(input("ano: "))
#ver se nao é divisivel por 100, e se é por 4 e 400
bissexto=(ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))
print("Seu ano é", bissexto)
