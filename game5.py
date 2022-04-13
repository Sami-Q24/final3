import random
import turtle
import time

ship = turtle.Turtle()
ship.speed(0)
ship.penup()
ship.shape('square')
ship.shapesize(stretch_wid=1, stretch_len=1)
ship.goto(-450, 0)
ship.color('red')

<<<<<<< Updated upstream
bullet = turtle.Turtle()
bullet.speed(0)
bullet.penup()
bullet.shape('circle')
bullet.color('blue')
bullet.shapesize(0.5)
bullety=1.5
def fire_bullet():
   x = ship.xcor()
   y = ship.ycor()
   bullet.setx(x)
   bullet.sety(y)
   if window.onkeypress(fire_bullet, "u"):
       bullet.sety(bullet.ycor() + bullety)

fire_bullet()
=======
def hide():
    ship.hideturtle()
>>>>>>> Stashed changes

def ship_left():
    y = ship.xcor()
    y = y - 15
    ship.setx(y)

def ship_right():
    y = ship.xcor()
    y = y + 15
    ship.setx(y)
def ship_up():
    y = ship.ycor()
    y = y + 15
    ship.sety(y)
def ship_down():
     y = ship.ycor()
     y = y - 15
     ship.sety(y)
def ship_up_right():
    x = ship.ycor()
    y = ship.xcor()
    x = x+15
    y = y+15
    ship.setx(y)
    ship.sety(x)

vel = -3/4


window = turtle.Screen()
window.setup(width=1000, height=400)
window.bgcolor('black')
window.tracer(0)


window.listen()
window.onkeypress(ship_left, "a")
window.onkeypress(ship_right, "d")
window.onkeypress(ship_up, "w")
window.onkeypress(ship_down, "s")


bullet = turtle.Turtle()
bullet.speed(0)
bullet.penup()
bullet.shape('circle')
bullet.color('blue')
bullet.shapesize(5)
bullety=1.5

def border():
    if ship.xcor()>480:
        ship.setx(480)
    elif ship.xcor()<-480:
        ship.setx(-480)
    elif ship.ycor()>175:
        ship.sety(175)
    elif ship.ycor()<-175:
        ship.sety(-175)

<<<<<<< Updated upstream
window.listen()
window.onkeypress(ship_left, "a")
window.onkeypress(ship_right, "d")
window.onkeypress(ship_up, "w")
window.onkeypress(ship_down, "s")
#window.onkeypress(ship_up_right, "w" and "d") this doesnt work....
=======

def fire_bullet():
   x = ship.xcor()
   y = ship.ycor()
   bullet.setx(x)
   bullet.sety(y)
   if window.onkeypress(fire_bullet, "u"):
       bullet.sety(bullet.ycor() + bullety)


def create_astroids(spawny, steps):
    astroid_ = turtle.Turtle()
    astroid_.penup()
    astroid_.goto(500, spawny)
    astroid_.color("yellow")
    astroid_.shape("square")
    astroid_.shapesize(stretch_wid=2, stretch_len=2)
    for i in range(steps):
        window.update()
        if (ship.xcor() + 10>astroid_.xcor()-20 and ship.xcor()+10 < astroid_.xcor()+20 and ship.ycor() > astroid_.ycor()-20 and ship.ycor() < astroid_.ycor()+20):
            hide()
        border()

        astroid_.setx(astroid_.xcor()+vel)
    astroid_.hideturtle()

for i in range(100):
    window.update()
    spawny = random.randint(-190, 190)
    vel = random.randint(2, 7)
    vel = -(vel/5)
    vel_steps = -vel
    print(vel)
    print("steps" + str(100//vel_steps))
    steps = int((1000//vel_steps) + 2)
    create_astroids(spawny, steps)

>>>>>>> Stashed changes


while True:
    window.update()
    border()

