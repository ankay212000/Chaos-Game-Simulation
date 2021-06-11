import turtle
import random

screen = turtle.Screen()
screen.title('Barnsley\'s Fern Chaos Game with Python Turtle')
screen.setup(500,500)
screen.setworldcoordinates(-6,-1,6,11)
screen.tracer(0,0)
turtle.hideturtle()
turtle.speed(0)
turtle.up()

n = 50000 # number of points to draw
p = (random.uniform(0,200),random.uniform(0,200)) # random starting point
t = turtle.Turtle()
t.up()
t.hideturtle()

def fern(p):
    r = random.uniform(0,1)
    if r < 0.01:
        p = (0,0.25*p[1]-0.4)
    elif r < 0.86:
        p = (0.95*p[0] + 0.005*p[1]-0.002, -0.005*p[0] + 0.93*p[1] + 0.5)
    elif r < 0.93:
        p = (0.035*p[0] - 0.2*p[1]-0.09, 0.16*p[0] + 0.04*p[1] + 0.02)
    else:
        p = (-0.04*p[0] + 0.2*p[1]+0.083, 0.16*p[0] + 0.04*p[1] + 0.12)
    return p   

for i in range(n):
    t.goto(p)
    t.dot(2,'green')  
    p=fern(p) 
    if i % 1000 == 0: # update for every 1000 moves, this part is for performance reason only
        t = turtle.Turtle() # use new turutle
        t.up()
        t.hideturtle()
        screen.update()        