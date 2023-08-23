import turtle
import math

def circ(cl, r):
    turtle.penup()
    turtle.color(cl)
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


def draw_flower(coll, sizz):
    window = turtle.Screen()
    window.bgcolor("white")
    hello = turtle.Turtle()
    hello.speed(0)
    hello.shape("triangle")
    hello.color(coll)
    for i in range(0, 36):
        draw_square(hello, sizz, coll)
        hello.right(10)

def draw_square(square, lll, cll):
    for i in range(2):
        square.begin_fill()
        square.fillcolor(cll)
        square.forward(lll)
        square.right(30)
        square.forward(lll)
        square.right(150)
        square.end_fill()


def petals(num, length):
    t.penup()
    t.home()
    t.pendown()
    t.setheading(0)
    t.speed(10)
    angle = 360 / num
    theta = 0
    t.fillcolor("green")  
    t.pencolor("green")   
    t.begin_fill()
    for i in range(num):
        t.setheading(theta)
        t.circle(length)
        theta += angle + 5  # Adding 5 degrees to the angle
    t.end_fill()


t = turtle.Turtle()
turtle.speed(5)
petals(8, 230) 
turtle.pen(pencolor="#770E13", pensize="1")
circ("#770E13", 400)
turtle.pen(pencolor="green", pensize="1")
circ("blue", 390)
turtle.pen(pencolor="#ECE19F", pensize="1")
circ("yellow", 380)

draw_flower("red", 190)
turtle.pen(pencolor="green", pensize="1")
petals(8, 160) 
circ("red", 260)
circ("#FFFF99", 250)
circ("#90EE90", 240) # Adjust the outline color for these petals
draw_flower("orange", 120)
draw_flower("red", 80)
draw_flower("#ECE20F", 60)

 



# Hide the turtle and display the artwork
turtle.hideturtle()
turtle.done()
