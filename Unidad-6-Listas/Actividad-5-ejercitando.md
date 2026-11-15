# Actividad 5 — Listas

## Enunciado

![Enunciado](imagenes/Captura%20de%20pantalla_14-11-2026_234721_chemical-isthmus-d04.notion.site.jpeg)

## Mi solución en Python

```python
# numeros = [3, 123, 4, 564, 23, 1, 95, 4]
def pares(numeros):
    cont=0
    for numero in numeros:
        if numero%2==0:
            cont+=1
    return(cont)
def impares(numeros):
    cont=0
    for numero in numeros:
        if numero%2 !=0:
            cont+=1
    return cont

print(pares(numeros))
print(impares(numeros))
```
