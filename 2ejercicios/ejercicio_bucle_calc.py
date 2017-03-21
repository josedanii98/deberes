def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b
 
while True:
    print """
teclee:
 
1 para sumar
2 para restar
3 para multiplicqar
4 para dividir
"""
    opcion=input(">")
    a=input("digite el primer numero:")
    b=input("digite el primer numero:")
    if opcion == 1:
        print suma(a,b)
    if opcion == 2:
        print resta(a,b)
 
    if opcion == 3:
        print multiplicar(a,b)
 
    if opcion == 4:
        print dividir(a,b)
 
    else:
        print "opcion incorrecta"
