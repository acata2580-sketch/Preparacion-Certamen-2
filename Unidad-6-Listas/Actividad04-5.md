# Actividad 5.5 — Ejercitando.

## Enunciado

![Captura de pantalla](Im%C3%A1genes/Captura%20de%20pantalla_15-11-2026_21395_chemical-isthmus-d04.notion.site.jpeg)

## Mi solución en Python

```python

respuestas_correctas = ["A", "C", "B", "D", "B"]
respuestas_alumno =    ["A", "B", "B", "D", "A"]

cont = 0
for i in range(len(respuestas_correctas)):
    if respuestas_correctas[i] == respuestas_alumno[i]:
        cont += 1
print(cont)
```

```python

#Si las listas no son del mismo largo:
"""
Al acceder a lista[i], el índice i debe existir
dentro de la lista. Si el índice está fuera de su
rango válido, Python genera un IndexError.
"""
cont=0
for i in range(len(respuestas_correctas)):
    if i <len(respuestas_alumno):
        if respuestas_correctas[i]==respuestas_alumno[i]:
            cont+=1
print(cont)

```
#<3
