import turtle

t = turtle.Turtle()

t.shape("turtle")
t.color("blue","red")
t.pensize(5)
t.speed(1)

t.begin_fill()
for _ in range(3):
  t.forward(100)
  t.left(120)
t.end_fill()

turtle.mainloop()