Dada la lista asignaturas, imrpime cada asignatura junto con su posición.
asignaturas = ["Matemáticas", "Lenguaje", "Historia", "Ciencias"]
# Muestra algo como: "0: Matemáticas", "1: Lenguaje", etc.
salida= ""
for i in range(len(asignaturas)):
    salida+= '"'+str(i)+ ":"+ asignaturas[i]+'", '
print(salida[:-2])
