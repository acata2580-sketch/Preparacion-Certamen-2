#Cambiar todos los elementos negativos de la lista `temperaturas` por 0
temperaturas = [20, -5, 13, -2, 0, 18]
for i in range(len(temperaturas)):
    if temperaturas[i]<0:
        temperaturas[i] = 0
print(temperaturas)
