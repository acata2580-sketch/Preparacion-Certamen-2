#Dada la lista asignaturas, imrpime cada asignatura junto con su posición.
asignaturas = ["Matemáticas", "Lenguaje", "Historia", "Ciencias"]
# Muestra algo como: "0: Matemáticas", "1: Lenguaje", etc.
salida= ""
for i in range(len(asignaturas)):
    salida+= '"'+str(i)+ ": "+ asignaturas[i]+'", ' #para que se imprima " como string, da Syntax Error poner """ y no deja ejecutar el programa.
print(salida[:-2])
