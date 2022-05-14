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

# Librerias que se saran
from random import randrange
from re import M
from signal import raise_signal
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Lista donde se almacenaran los colores del juego
color = []

# Paleta de colores en el juego
y = "yellow"
g = "green" 
b = "blue" 
m = "magenta"
hp = "hotpink"

# Random del color de la serpiente 
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
    
# Se crea una funcion que asigna un color diferente cada vez que se corre el juego
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
    # Change snake direction.
    aim.x = x
    aim.y = y


def inside(head):
    # Es para comprobar que la cabeza de la serpiente no ha chocado con ningun limite
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    # Hace que la serpiente se mueva por segmente 
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
        # Aqui se aplican los limites de la comida haciendo que si la serpiente quiere sar por alguno de los lados, esta vaya hacia la 
        # direccion opuesta
        comida = randrange(0,20)
        if food.x == 190:
            food.x += -20
        if food.x == -190:
            food.x += 20
        if food.y == 190:
            food.y += -20
        if food.y == -190:
            food.y += 20 

        # Aqui se modifica la posicion de la comida para que este cambiando de posicion cada que la variable comida cambie de valor            
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
        # La lista que se habia creado con colores previamente y en donde toma el color en la posicion 0 y se lo asigna a la serpiente, mientras
        # que el siguiente valor va a ser el color de la comida, y este cambia cada que la serpiente come   
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