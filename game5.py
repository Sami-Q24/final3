import turtle

win = turtle.Screen()
win.screensize(canvwidth=400, canvheight=400)
win.bgcolor("Black")
win.title("Space Shooters")


ship = turtle.Turtle()
ship.speed(0)
ship.penup()
ship.shape('square')
ship.goto(0, -200)
ship.color('red')

def ship_left():
    y = ship.xcor()
    y = y - 15
    ship.setx(y)

def ship_right():
    y = ship.xcor()
    y = y + 15
    ship.setx(y)

window.onkeypress(ship_left, "a")
window.onkeypress(ship_right, "d")

while True:
    win.update()