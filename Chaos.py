import turtle
import random
import time

screen = turtle.Screen()
screen.title('Chaos Game with Python Turtle')
screen.setup(500,500)
#screen.setworldcoordinates(-6,-1,6,11)
screen.tracer(0,0)
turtle.hideturtle()
turtle.speed(0)
turtle.up()

def pentagon():
    A = (100,0)
    B = (5,69)
    C = (41,181)
    D = (159,181)
    E = (195,69)
    return (A,B,C,D,E) 

def traingle():
    A=(100,0)
    B=(13,150)
    C=(187,150)
    return (A,B,C)

def square():
    A=(171,29)
    B=(29,29)
    C=(29,171)
    D=(171,171)
    return (A,B,C,D)

V = pentagon()     #Change this for different shapes

for v in V:
    turtle.goto(v)
    turtle.dot('red')

n = 50000 # number of points to draw
p = (random.uniform(0,200),random.uniform(0,200)) # random starting point
t = turtle.Turtle()
t.up()
t.hideturtle()

def fractal(V,p):
    r=random.randrange(len(V))      
    p = ((V[r][0]+p[0])/2,(V[r][1]+p[1])/2)
    return p

r = random.randrange(len(V))

for i in range(n):
    t.goto(p)
    t.dot(2,'black')
    p=fractal(V,p) 
    #time.sleep(0.2)    
    if (i % 1000 == 0): # update for every 1000 moves, this part is for performance reason only
        t = turtle.Turtle() # use new turutle
        t.up()
        t.hideturtle()
        screen.update()