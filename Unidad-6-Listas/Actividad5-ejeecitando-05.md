# Actividad 5.5 — Ejercitando.

## Enunciado

![Captura de pantalla](Im%C3%A1genes/Captura%20de%20pantalla_15-11-2026_205142_chemical-isthmus-d04.notion.site.jpeg)

## Mi solución en Python

```python
tickets = ['G366', 'B480', 'A123', 'H234', 'A234', 'G566', 'G333']
personas = ['kiwi', 'gordon ', 'sneki ', 'bonobo ', 'tux', 'sakila ', 'wilber ']
tickets_ordenados = tickets[:]
tickets_ordenados.sort()

for x in range(len(tickets_ordenados)):
    elemento = tickets_ordenados[x]
    i= tickets.index(elemento)
    print(x+1, personas[i])

```
#<3
