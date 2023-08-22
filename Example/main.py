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

# Draw filled triangles around a circle
radius = 20
num_triangles = 12
square_side_length = 50
t.fillcolor("red")

t.penup()
t.goto(0, 110)
t.pendown()
t.begin_fill()

# turn pen to 45 degree
t.left(45)

for _ in range(4):
    t.forward(square_side_length)  # Move the turtle forward by side_length units
    t.left(90)  # Turn left by 90 degrees

t.end_fill()

# Draw the triangles
for _ in range(num_triangles):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    
    for _ in range(3):
        t.forward(radius * 2)  # Each side of the equilateral triangle
        t.left(120)  # Turn 120 degrees

    t.end_fill()
    t.left(360 / num_triangles)


# Hide the turtle
t.hideturtle()

# Keep the window open until it's closed by the user
turtle.done()
