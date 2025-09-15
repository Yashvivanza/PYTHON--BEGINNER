import turtle

# 1. Set up the screen
screen = turtle.Screen()
screen.title("Star Drawing with Turtle")
screen.bgcolor("lightblue")   # background color

# 2. Create turtle (pen)
pen = turtle.Turtle()
pen.pensize(3)                # line thickness
pen.speed(3)                  # drawing speed

# 3. Set border (pen) color and fill color
pen.color("red", "yellow")    # border = red, fill = yellow

# 4. Draw filled star
pen.begin_fill()

for _ in range(5):            # 5 sides → star
    pen.forward(200)          # move forward
    pen.right(144)            # turning angle for star

pen.end_fill()

# 5. Hide turtle and finish
pen.hideturtle()
turtle.mainloop()
