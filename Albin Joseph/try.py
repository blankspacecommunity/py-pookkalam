import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pookkalam Design")

# Create a turtle
t = turtle.Turtle()
t.speed(500)


# Draw the circle 1
t.penup()
t.goto(0, -197)
t.begin_fill()
t.fillcolor("#fb5902")
t.circle(197)
t.pendown()
t.end_fill()

t.penup()
t.goto(-72.5, -175)
t.pendown()
t.begin_fill()
t.fillcolor("white")


for _ in range(8):
    t.penup()
    t.forward(145) 
    t.left(45) 
    t.pendown()
t.end_fill()
t.penup()
t.pendown()


t.penup()
t.goto(-70, -169)
t.pendown()
t.begin_fill()
t.fillcolor("#701c0b")


for _ in range(8):
    t.penup()
    t.forward(140) 
    t.left(45) 
    t.pendown()
t.end_fill()
t.penup()
t.pendown()


t.penup()
t.goto(-67.5, -163)
t.pendown()
t.begin_fill()
t.fillcolor("white")


for _ in range(8):
    t.penup()
    t.forward(135) 
    t.left(45) 
    t.pendown()
t.end_fill()
t.penup()
t.pendown()



for _ in range(24):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor("#f6ff06")
    
    for _ in range(3):
        t.penup()
        t.forward(81* 2)  # Each side of the equilateral triangle
        t.left(120)  # Turn 120 degrees
        t.pendown()
    t.end_fill()
    t.penup()
    t.left(360 / 24)
    t.pendown()



t.left(7.5)
for _ in range(24):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor("violet")
    
    for _ in range(3):
        t.penup()
        t.forward(76* 2)  # Each side of the equilateral triangle
        t.left(120)  # Turn 120 degrees
        t.pendown()
    t.end_fill()
    t.penup()
    t.left(360 / 24)
    t.pendown()

t.left(30)
for _ in range(8):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor("white")
    
    for _ in range(3):
        t.penup()
        t.forward(71* 2)  # Each side of the equilateral triangle
        t.left(120)  # Turn 120 degrees
        t.pendown()
    t.end_fill()
    t.penup()
    t.left(360 / 8)
    t.pendown()

t.left(7.5)
for _ in range(24):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor("#8f0707")
    
    for _ in range(3):
        t.penup()
        t.forward(63* 2)  # Each side of the equilateral triangle
        t.left(120)  # Turn 120 degrees
        t.pendown()
    t.end_fill()
    t.penup()
    t.left(360 / 24)
    t.pendown()



for _ in range(24):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor("yellow")
    
    for _ in range(3):
        t.penup()
        t.forward(58* 2)  # Each side of the equilateral triangle
        t.left(120)  # Turn 120 degrees
        t.pendown()
    t.end_fill()
    t.penup()
    t.left(360 / 24)
    t.pendown()

t.right(45)
t.penup()
t.begin_fill()
t.goto(-67.5, -163)
t.fillcolor("#f72525")
t.left(90)
for _ in range(8):
    t.penup()
    t.forward(326.5)
    t.right(135)
    t.pendown()

t.end_fill()
t.penup()
t.pendown()

2
t.penup()
t.right(90)
t.goto(0, -95)
t.begin_fill()
t.fillcolor("#ff73da")
t.circle(96)
t.pendown()
t.end_fill()


t.penup()
t.goto(0,-93)
t.left(45)
t.begin_fill()
t.fillcolor("#ff8c42")
for _ in range(4):
    t.penup()
    t.forward(132)
    t.left(90)
    t.pendown()
t.end_fill()
t.penup()
t.pendown()


t.penup()
t.goto(0,0)
t.left(45)
t.begin_fill()
t.fillcolor("#cfe8ef")
for _ in range(4):
    t.penup()
    
    t.forward(66)
    t.left(90)
    t.forward(66)
    t.left(90)
    t.forward(39)
    t.left(135)
    t.forward(28)
    t.right(90)
    t.forward(66)
    t.left(45)
    t.pendown()
t.end_fill()
t.penup()
t.pendown()



t.penup()
t.left(90)
t.goto(0,6)
t.begin_fill()
t.fillcolor("#701c0b")
t.circle(6)
t.pendown()
t.end_fill()
# t.penup()
# t.goto(27,-163)
# x=40.5
# y=-163
# t.pendown()
# t.begin_fill()
# t.fillcolor("red")
# w=270
# l=192
# t.left(45)
# for _ in range(2):
#     for _ in range(2):
#         t.penup()
#         t.forward(l)
#         t.left(90)
#         t.forward(w)
#         t.left(90)
#         t.pendown()
#     t.goto(x-27,y)
#     w-=30
#     l+=30
# t.end_fill()
# t.penup()
# t.pendown()
t.penup()
t.goto(1000,1000)
t.pendown()
turtle.done()