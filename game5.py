import turtle
import time

window = turtle.Screen()
window.setup(width=1000, height=400)
window.bgcolor('black')
window.tracer(0)

ship = turtle.Turtle()
ship.speed(0)
ship.penup()
ship.shape('square')
ship.goto(-450, 0)
ship.color('red')

vel = -1

def create_astroids():
    astroid_ = turtle.Turtle()
    astroid_.penup()
    astroid_.goto(500, 0)
    astroid_.color("yellow")
    astroid_.shape("square")
    astroid_.shapesize(stretch_wid=2, stretch_len=2)
    for i in range(1020):
        window.update()
        astroid_.setx(astroid_.xcor()+vel)
    astroid_.hideturtle()

create_astroids()

def ship_left():
    y = ship.xcor()
    y = y - 15
    ship.setx(y)

def ship_right():
    y = ship.xcor()
    y = y + 15
    ship.setx(y)

<<<<<<< Updated upstream
def border():
    if ship.xcor()>200:
        ship.setx(200)
    elif ship.xcor()<-200:
        ship.setx(-200)
=======
def ship_down():
    x = ship.ycor()
    x = x - 15
    ship.sety(x)

def ship_up():
    x = ship.ycor()
    x = x + 15
    ship.sety(x)

def ship_up_right():
    x = ship.ycor()
    y = ship.xcor()
    x = x+15
    y = y+15
    ship.setx(y)
    ship.sety(x)

>>>>>>> Stashed changes

window.listen()
window.onkeypress(ship_left, "a")
window.onkeypress(ship_right, "d")
window.onkeypress(ship_up, "w")
window.onkeypress(ship_down, "s")
window.onkeypress(ship_up_right, "w" and "d")

while True:
    window.update()
    border()

