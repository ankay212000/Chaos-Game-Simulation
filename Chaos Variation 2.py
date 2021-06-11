import turtle
import random

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
print(V)
for v in V:
    turtle.goto(v)
    turtle.dot('red')

n = 50000 # number of points to draw
p = (random.uniform(0,200),random.uniform(0,200)) # random starting point
t = turtle.Turtle()
t.up()
t.hideturtle()

def variaton_square(V,n,p,t):
    r = random.randrange(len(V))
    chose=[r]
    for i in range(n):
        t.goto(p)
        t.dot(2,'black')
        if(len(chose)>2):
            if(chose[-1]==chose[-2]):
                if(r==0):
                    r=2
                elif(r==1):
                    r=3
                elif(r==2):
                    r=0
                elif(r==3):
                    r=1
            else:
                r=random.randrange(len(V))         
        else:
            r=random.randrange(len(V))
        chose.append(r)
        try:
            p = ((V[r][0]+p[0])/2,(V[r][1]+p[1])/2) # go to mid point between the random vertex and point
        except:
            print(r)
            break               
        if (i % 1000 == 0): # update for every 1000 moves, this part is for performance reason only
            t = turtle.Turtle() # use new turutle
            t.up()
            t.hideturtle()
            screen.update()

def variation_pentagon(V,n,p,t):
    r = random.randrange(len(V))
    chose=[r]
    for i in range(n):
        t.goto(p)
        t.dot(2,'black')
        if(len(chose)>2):
            if(chose[-1]==chose[-2]):
                if(r==0):
                    l=[2,3]
                    r=l[random.randrange(len(l))]
                    #r=2
                elif(r==1):
                    l=[4,3]
                    r=l[random.randrange(len(l))]
                    #r=3
                elif(r==2):
                    l=[0,4]
                    r=l[random.randrange(len(l))]
                    #r=0
                elif(r==3):
                    l=[1,0]
                    r=l[random.randrange(len(l))]
                    #r=1
                elif(r==4):
                    l=[2,1]
                    r=l[random.randrange(len(l))]
            else:
                r=random.randrange(len(V))         
        else:
            r=random.randrange(len(V))
        chose.append(r)
        try:
            p = ((V[r][0]+p[0])/2,(V[r][1]+p[1])/2) # go to mid point between the random vertex and point
        except:
            print(r)
            break               
        if (i % 1000 == 0): # update for every 1000 moves, this part is for performance reason only
            t = turtle.Turtle() # use new turutle
            t.up()
            t.hideturtle()
            screen.update()

if(len(V)==5): 
    variation_pentagon(V,n,p,t)
elif(len(V)==4):    
    variaton_square(V,n,p,t)
else:
    print("this variation not possible for triangle")        