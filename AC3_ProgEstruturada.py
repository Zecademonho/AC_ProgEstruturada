"""
AC3- Programacao Estruturada
"""

"""
1_Salario
"""
#pedir input ao user
salario=float(input("insira o valor do salario: "))


#calcular a porcentagem de aumento
def calc_sal(salario):
    
    if salario <= 280:
        prct = 0.2
        
    elif  salario <= 700 :
        prct = 0.15
         
    elif salario <= 1500 :
        prct = 0.1
         
    elif salario > 1500 :
        prct = 0.05
        
    aumento= salario * prct
    nvsl= salario + aumento
    
    print ( "O salario antigo era de ", salario , "O percentual de aumento é de ", 100 * prct,\
            "O valor do aumento é de ", aumento , "O novo salario é de ", nvsl )
    
        
    
calc_sal(salario)


"""
2_Ver dia da semana
"""

dia = input("Digite o dia para descubrir o numero da semana: ")
def cli():
    match dia:
        case "1" :
            print("Domingo")
        case "2" :
            print("Segunda")
        case "3" :
            print("Terca")
        case "4" :
            print("Quarta")
        case "5":
            print("Quinta")
        case "6" :
            print("Sexta")
        case "7" :
            print("Sabado")
        case _:
            print("valor invalido")

cli()


"""
3_Baskara
"""
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))

def baskara(a, b, c):
    delta= (b**2 - 4 * a * c)
    x1= ((-b + (delta)**1/2)/ (2 * a))
    x2= ((-b - (delta)**1/2)/ (2 * a))
    if a==0:
        return "Equacao não é do segundo grau"
    elif delta < 0:
        return "Não possui raizes reais"
    elif delta == 0 :
        print("Possui apenas uma raiz real")
        return x1
    else: 
        return x1, x2
    
print(baskara(a, b, c))
