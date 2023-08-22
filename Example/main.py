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

# Draw filled triangles around a circle

square_side_length = 50
t.fillcolor("red")

# t.penup()
# t.goto(0, 110)
# t.pendown()
# t.begin_fill()

# # turn pen to 45 degree
# t.left(45)

# for _ in range(4):
#     t.forward(square_side_length)  # Move the turtle forward by side_length units
#     t.left(90)  # Turn left by 90 degrees
# t.end_fill()

# t.left(225)

# t.penup()
# t.goto(25, 110)
# t.pendown()
# t.begin_fill()

# # turn pen to 45 degree
# t.left(45)

# for _ in range(4):
#     t.forward(square_side_length)  # Move the turtle forward by side_length units
#     t.left(90)  # Turn left by 90 degrees
# t.end_fill()

radius = 90
num_triangles = 12
# Draw the triangles
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

radius = 80
t.left(45)
# Draw the triangles
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

radius = 70
t.left(45)
# Draw the triangles
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

radius = 60
t.left(45)
# Draw the triangles
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
# # Draw the circle 3
# t.goto(0, -80)
# t.pendown()
# t.begin_fill()
# t.fillcolor("red")
# t.circle(80)
# t.end_fill()

# # Draw the circle 4
# t.goto(0, -70)
# t.pendown()
# t.begin_fill()
# t.fillcolor("yellow")
# t.circle(70)
# t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open until it's closed by the user
turtle.done()
