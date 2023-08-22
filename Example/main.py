import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pookkalam Design")

# Create a turtle
t = turtle.Turtle()
t.speed(10)

# Draw the circle 1
t.penup()
t.goto(0, -200)
t.begin_fill()
t.fillcolor("#d31f4b")
t.circle(200)
t.pendown()
t.end_fill()

# Draw the circle 2
t.penup()
t.goto(0, -190)
t.begin_fill()
t.fillcolor("#fb5902")
t.circle(190)
t.pendown()
t.end_fill()

# Draw filled triangles inside the circle
radius = 90
num_triangles = 12

# layer 1
for _ in range(num_triangles):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor("white")
    
    for _ in range(3):
        t.penup()
        t.forward(radius * 2)  # Each side of the equilateral triangle
        t.left(120)  # Turn 120 degrees
        t.pendown()
    t.end_fill()
    t.penup()
    t.left(360 / num_triangles)
    t.pendown()

# layer 2
radius = 80
t.left(45)
for _ in range(num_triangles):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor("#f6ff06")
    
    for _ in range(3):
        t.penup()
        t.forward(radius * 2)  # Each side of the equilateral triangle
        t.left(120)  # Turn 120 degrees
        t.pendown()
    t.end_fill()
    t.penup()
    t.left(360 / num_triangles)
    t.pendown()

# layer 3
radius = 70
t.left(45)
for _ in range(num_triangles):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor("#ff6401")
    
    for _ in range(3):
        t.penup()
        t.forward(radius * 2)  # Each side of the equilateral triangle
        t.left(120)  # Turn 120 degrees
        t.pendown()
    t.end_fill()
    t.penup()
    t.left(360 / num_triangles)
    t.pendown()

# layer 4
radius = 60
t.left(45)
for _ in range(num_triangles):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor("#ad0308")
    
    for _ in range(3):
        t.penup()
        t.forward(radius * 2)  # Each side of the equilateral triangle
        t.left(120)  # Turn 120 degrees
        t.pendown()
    t.end_fill()
    t.penup()
    t.left(360 / num_triangles)
    t.pendown()

# Draw the circle 3
t.penup()
t.goto(55, 55)
t.begin_fill()
t.fillcolor("#f6ff06")
t.circle(80)
t.pendown()
t.end_fill()

# Draw the circle 4
t.penup()
t.goto(40, 40)
t.begin_fill()
t.fillcolor("#ff6401")
t.circle(60)
t.pendown()
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open until it's closed by the user
turtle.done()
