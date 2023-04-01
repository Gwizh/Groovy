import random
import turtle

# Set up the canvas
canvas = turtle.Screen()
canvas.setup(600, 600)  # canvas size in pixels
canvas.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed("fastest")
t.hideturtle()

# Define a function to draw a diagonal rectangle at a given position and color
def draw_rectangle(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.setheading(45)
    for i in range(2):
        t.forward(40)
        t.right(90)
        t.forward(80)
        t.right(90)
    t.end_fill()

# Generate diagonal rectangles until the canvas is filled with shapes
while True:
    x = random.randint(-280, 240)
    y = random.randint(-240, 280)
    if x == 240 and y == 240:
        break  # exit the loop if the canvas is filled with shapes
    r = random.randint(0, 255)/255
    g = random.randint(0, 255)/255
    b = random.randint(128, 255)/255  # random blue shade
    color = (r, g, b)
    draw_rectangle(x, y, color)

# Exit the program
turtle.done()