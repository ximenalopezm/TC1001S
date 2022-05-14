"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""
# Editado por 
# Kevin Valdez - A01254336
# Daniela Ruiz - A01254229
# Ximena López - A01254325
# Gustavo Betancourt - A01252532

from turtle import *
import turtle

from freegames import vector


def line(start, end):
    # Funcion que dibuja las lineas
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    # Funcion que dibuja cuadrados
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Función para dibujar un círculo
def circle(start, end):

    t = turtle
    r = 50
    t.circle(r) 

    pass  # TODO

# Función para dibujar un rectángulo
def rectangle(start, end):
  
    t = turtle
 
    l = 100
    w = 50
    
    t.forward(l) 
    t.left(90) 
    
    t.forward(w) 
    t.left(90) 
    
    t.forward(l) 
    t.left(90) 
    
    t.forward(w) 
    t.left(90) 

    pass  # TODO

# Función para dibujar un triángulo
def triangle(start, end):

    t = turtle.Turtle()  
    
    t.forward(90)  
       
    t.left(120) 

    t.forward(90)  

    t.left(120)

    t.forward(90)  

      
    pass  # TODO


def tap(x, y):
    # Aqui se inicia el punto de dibujo
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

# Colores agregados
onkey(lambda: color('pink'), 'P')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()