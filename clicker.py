# why bro

import turtle

wn = turtle.Screen()
wn.title("Budget Cookie Clicker")
wn.bgcolor("black")

wn.register_shape("cookie.gif")

cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)

clicks = 0

turtle.hideturtle()
turtle.color("white")
turtle.penup()
turtle.goto(0, 400)
turtle.write(clicks)

def clicked(x, y):
    global clicks
    clicks += 1
    turtle.clear()
    print(clicks)
    turtle.color("white")
    turtle.write(clicks)
    turtle.hideturtle()

cookie.onclick(clicked)

wn.mainloop()