# Creado por 
# Kevin Valdez - A01254336
# Daniela Ruiz - A01254229
# Ximena Lopez - A01254325
# Gustavo Betancourt - A01252532

# llamamos a las librerias utilizadas
import turtle
import math
import random
import time
import winsound

WIDTH, HEIGHT = 600, 600

# Pantalla del menu

menu = turtle.Screen()
menu.setup(WIDTH, HEIGHT)
menu.bgcolor("black")
menu.title("Los Invasores del Norte")
menu.bgpic("menu.gif")
menu.update()
time.sleep(5)

# Set up de la ventana
pantalla = turtle.Screen()
pantalla.setup(WIDTH, HEIGHT)
pantalla.bgcolor("black")
pantalla.title("Los Invasores del Norte")
pantalla.bgpic("fondo.gif")

# Asignamos la figura de nuestras tortugas
turtle.register_shape("alien.gif")
turtle.register_shape("nave.gif")
turtle.register_shape("bala.gif")
turtle.register_shape("balav.gif")
turtle.register_shape("exp1.gif")

# Contador puntaje
score = 0

# Draw the pen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Puntaje: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Crea al jugador
navecita = turtle.Turtle()
navecita.shape("nave.gif")
navecita.penup()
navecita.setposition(0,-250)
#navecita.setheading(90)

# Velocidad del jugador
navecitaspeed = 15

# Cantidad de aliens enemigos
numero_de_aliens = 10
# Lista vacia de aliens enemigos
aliens = []

# Agrega los aliens a la lista
for i in range(numero_de_aliens):
    # crea el enemigo
    aliens.append(turtle.Turtle())

# Posiciona a los aliens
for alien in aliens:
    alien.shape("alien.gif")
    alien.penup()
    x = random.randint(-200, 200)
    y =  random.randint(100, 250)
    alien.setposition(x, y)

# Inicia la musica del juego
winsound.PlaySound("audiosJuego.wav", flags = winsound.SND_ASYNC)

# Velocidad de los aliens
alienspeed = 5

# Explosión de los aliens
explosion1 = turtle.Turtle()
explosion1.shape("exp1.gif")

explosion1.hideturtle()


# Crea las balas de la navecita
bala = turtle.Turtle()
bala.color("pink")
bala.shape("bala.gif") # CAMBIAR
bala.penup()
bala.speed(0)
bala.setheading(90)
bala.shapesize(0.5,0.5)
bala.hideturtle()

# Velocidad de la bala
balaspeed = 45

bulletv = turtle.Turtle()
bulletv.color("green")
bulletv.shape("balav.gif")
bulletv.penup()
bulletv.speed(0)
bulletv.setheading(90)
bulletv.shapesize(0.5,0.5)
bulletv.hideturtle()

bulletvspeed = 75

# define estado_bala
# ready - listo para disparar
# fire - bala se esta disparando
estado_bala = "ready"
bulletvstate = "ready"

# Mueve en el eje X la navecita a la izquierda
def hacia_izq():
    x = navecita.xcor()
    x -= navecitaspeed
    if x < -280:
        x = -280
    navecita.setx(x)

# Mueve en el eje X la navecita a la derecha
def hacia_der():
    x = navecita.xcor()
    x += navecitaspeed
    if x > 280:
        x = 280
    navecita.setx(x)

def fuego_bala():
    # Declara estado_bala como global por si necesitamos cambiarle
    global estado_bala
    if estado_bala == "ready":
        estado_bala = "fire"
        # Coloca la bala arribita de la navecita
        x = navecita.xcor()
        y = navecita.ycor() + 20
        bala.setposition(x,y)
        bala.showturtle()

def fire_bulletv():
    # Declara estado_bala como global por si necesitamos cambiarle
    global bulletvstate
    if bulletvstate == "ready":
        bulletvstate = "fire"
        # Coloca la bala arribita de la navecita
        x = navecita.xcor()
        y = navecita.ycor() + 10
        bulletv.setposition(x,y)
        bulletv.showturtle()

# Colision alien - bala
def Choque_alien_bala(bala, alien):
    distancia = math.sqrt(math.pow(bala.xcor()-alien.xcor(),2)+math.pow(bala.ycor()-alien.ycor(),2))
    if distancia < 25:
        return True
    else:
        return False

# Colision alien - navecita
def Choque_alien_navecita(navecita, alien):
    distancia = math.sqrt(math.pow(navecita.xcor()-alien.xcor(),2)+math.pow(navecita.ycor()-alien.ycor(),2))
    if distancia < 30:
        return True
    else:
        return False

# Crea las teclas para jugar
turtle.listen()
turtle.onkey(hacia_izq, "a") 
turtle.onkey(hacia_der, "d")
turtle.onkey(fuego_bala, "space")
turtle.onkey(fire_bulletv, "g")

# Bucle del juego
Perdiste_Crack = False
aliens_perdidos = 0

while True:

    for alien in aliens:
        # Mueve el alien
        x = alien.xcor()
        x += alienspeed
        alien.setx(x)

        # Mueve el alien pa bajo y pa tras
        if alien.xcor() > 270:
            # Mueve el alien hacia abajo
            for e in aliens:
                y = e.ycor()
                y -= 40
                e.sety(y)
                if e.ycor() < -285 and Perdiste_Crack == False:
                    e.hideturtle()
                    aliens_perdidos += 1
                    if aliens_perdidos == 5:
                        Perdiste_Crack = True
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    e.setposition(x, y)
                    e.showturtle()
            # Cambia la direccion del alien
            alienspeed *= -1

        if alien.xcor() < -270:
            # Mueve el alien hacia abajo
            for e in aliens:
                y = e.ycor()
                y -= 40
                e.sety(y)
                if e.ycor() < -285 and Perdiste_Crack == False:
                    e.hideturtle()
                    aliens_perdidos += 1
                    if aliens_perdidos ==5:
                        Perdiste_Crack = True
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    e.setposition(x, y)
                    e.showturtle()
            # Cambia la direccion del alien
            alienspeed *= -1

        # Checa si el alien y la bala chocan
        if Choque_alien_bala(bala, alien):
            # Resetea la bala
            bala.hideturtle()
            estado_bala = "ready"
            bala.setposition(0, -400)

            explosion1.penup()
            explosion1.speed(0)
            explosion1.showturtle()
            explosion1.setposition(x,y)

            # Resetea el alien
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            alien.setposition(x, y)
            alienspeed += 0.5
            # actualiza el score
            score += 1
            scorestring = "Puntaje: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            explosion1.hideturtle()

        if Choque_alien_bala(bulletv, alien):
            # Lo mismo que lo de arriba pero para la bala verde
            explosion1.penup()
            explosion1.speed(0)
            explosion1.showturtle()
            explosion1.setposition(x,y)
            
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            alien.setposition(x, y)
            alienspeed += 0.5
            # update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            explosion1.hideturtle()

        # Checa si el alien y la navecita chocan
        if Choque_alien_navecita(navecita, alien):
            Perdiste_Crack = True
            
        # Oculta todo y muestra la pantalla de fin de juego, si el jugador perdio
        if Perdiste_Crack == True:
            winsound.PlaySound(None, winsound.SND_PURGE)
            navecita.hideturtle()
            bala.hideturtle()
            for e in aliens:
                e.hideturtle()
            pantalla.bgpic("gameOver.gif")
            score_pen.clear()
            score_pen.setposition(0, -100)
            score_pen.write(scorestring, False, align="center", font=("Arial", 14, "normal"))
            break

    # Mueve la vala
    if estado_bala == "fire":
        y = bala.ycor()
        y += balaspeed
        bala.sety(y)

    if bulletvstate == "fire":
        y = bulletv.ycor()
        y += bulletvspeed
        bulletv.sety(y)

    # Checa si la bala llega al techo
    if bala.ycor() > 275:
        bala.hideturtle()
        estado_bala = "ready"

    if bulletv.ycor() > 275:
        bulletv.hideturtle()
        bulletvstate = "ready"

turtle.done()