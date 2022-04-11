import turtle

window = turtle.Screen()
window.setup(width=500, height=500)
window.bgcolor('black')
window.tracer(0)

ship = turtle.Turtle()
ship.speed(0)
ship.penup()
ship.shape('square')
ship.goto(0, -200)
ship.color('red')

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
