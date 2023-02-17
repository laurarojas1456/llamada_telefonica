# Programa para determinar la cantidad a pagar de una llamada telefonica 

print("---------------------------------------------")
print("---------Llamada Telefónica------------------")
print("---------------------------------------------")

# input
x = int(input ("digite el valor de x: "))

# processing
if x>3:
    y = x-3
    f = y*50
    j = f+300
    print("El costo de la llamada fue " +str(j)+ " el costo adicional fue de " +str(f))
else:
    print("El costo de la llamada es de 300")


    