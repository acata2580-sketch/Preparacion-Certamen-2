# Actividad 5.3 — Ejercitando.

## Enunciado

![Captura de pantalla](Im%C3%A1genes/Captura%20de%20pantalla_15-11-2026_211346_chemical-isthmus-d04.notion.site.jpeg)
![Captura de pantalla](Im%C3%A1genes/Captura%20de%20pantalla_15-11-2026_211531_chemical-isthmus-d04.notion.site.jpeg)

## Mi solución en Python

```python
puntajes = [1, 2, 2.5, 3, 1, 0, 1 , 0, 5, 3.5]
def mejor_pregunta(p):
    for  i in range(len(puntajes)):
        if puntajes[i]==max(puntajes):
            numero = i+1
            return numero

def puntaje_maximo(p):
    return len(puntajes)*5

def nota_final(p):
    cien= puntaje_maximo(p)
    porcentaje = (sum(p)*100)/50
    return porcentaje



print(mejor_pregunta(puntajes)) # 9
print(puntaje_maximo(puntajes)) # 50
print(nota_final(puntajes)) # 38.0
                        
    
```
#<3
