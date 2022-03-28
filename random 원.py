import random
import turtle

t=turtle.Turtle()
t.shape("turtle")
t.speed(50)
for i in range(10):
    r=random.randrange(1, 100)
    f=random.randrange(-100, 100)
    w=random.randrange(-100, 100)
    t.circle(r)
    t.penup()
    t.goto(f,w)
    t.pendown()
