import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pookkalam Design")

# Create a turtle
t = turtle.Turtle()
t.speed(10)
t.penup()
t.color("white")

# Draw the circle 1
t.goto(0, -200)
t.pendown()
t.begin_fill()
t.fillcolor("red")
t.circle(200)
t.end_fill()

# Draw the circle 2
t.goto(0, -190)
t.pendown()
t.begin_fill()
t.fillcolor("yellow")
t.circle(190)
t.end_fill()

# Draw the circle 3
t.goto(0, -80)
t.pendown()
t.begin_fill()
t.fillcolor("red")
t.circle(80)
t.end_fill()

# Draw the circle 4
t.goto(0, -70)
t.pendown()
t.begin_fill()
t.fillcolor("yellow")
t.circle(70)
t.end_fill()

# Draw the circle 5
t.goto(0, -20)
t.pendown()
t.begin_fill()
t.fillcolor("red")
t.circle(20)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open until it's closed by the user
turtle.done()
