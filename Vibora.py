"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

# Editado por 
# Kevin Valdez - A01254336
# Daniela Ruiz - A01254229
# Ximena López - A01254325
# Gustavo Betancourt - A01252532

from random import randrange
from re import M
from signal import raise_signal
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

"""Lista donde se almacenaran los colores de la serpiente y la comida """
color = []

"""Colores seleccionados"""
y = "yellow"
g = "green" 
b = "blue" 
m = "magenta"
hp = "hotpink"
"""Random del color de la serpiente""" 
nn = randrange(0,4)
if nn == 0 :
    color.append(y)
if nn == 1:
    color.append(g)
if nn == 2:
    color.append(b) 
if nn == 3:
    color.append(m) 
if nn == 4:
    color.append(hp)
    

"""Funcion que da colores random a la lista que le manda los colores a la comida"""
def colors(color):
    y = "yellow"
    g = "green" 
    b = "blue" 
    m = "magenta"
    hp = "hotpink"
    c = [y,g,b,m,hp]
    nn = randrange(0,4)
    while c[nn] != color[0] and c[nn] != c[-1]:
        if nn == 0:
            color.append(y)
        if nn == 1:
            color.append(g)
        if nn == 2:
            color.append(b) 
        if nn == 3:
            color.append(m) 
        if nn == 4:
            color.append(hp)
        return(color)    

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        
    else:
        """Aqui se le aplican los bordes a la comida haciendo que
        se mueva a la direccion opuesta de la pared por donde quiere salir"""
        comida = randrange(0,20)
        if food.x == 190:
            food.x += -20
        if food.x == -190:
            food.x += 20
        if food.y == 190:
            food.y += -20
        if food.y == -190:
            food.y += 20 

        """Aqui se modifican los vectores de la comida para que se mueva de posicion"""            
        if comida == 0:
            food.x += 10
        elif comida == 1:
            food.y += 10
        elif comida == 2:
            food.x += 10
        elif comida == 3:
            food.y += 10
        snake.pop(0)

    clear()
    
    
    colors(color)           


    for body in snake:
        """Aqui se modifico el valor del color por el primero de la lista siendo el de la serpiente 
        y los demas siendo la posicion en su lista vinculada al largo de la serpiente"""    
        square(body.x, body.y, 9, color[0])
    square(food.x, food.y, 9, color[len(snake)])   
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()