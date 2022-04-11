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
    for i in range(1000):
        window.update()
        astroid_.setx(astroid_.xcor()+vel)

create_astroids()

def ship_left():
    y = ship.xcor()
    y = y - 15

def ship_right():
    y = ship.xcor()
    y = y + 15

window.onkeypress(ship_left, "a")
window.onkeypress(ship_right, "d")
while True:
    window.update()