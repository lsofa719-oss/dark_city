from turtle import *
from random import *
from city import *

window = rect
build = rect

def pen_move(x, y):
    penup()
    goto(x, y)
    pendown()

def stein(x, y, r):
    pen_move(x, y)
    color('#dbbfa1')
    begin_fill()
    circle(r)
    end_fill()


pensize(3)
speed(0)
#sky

rect(-250, -240, 500 , 470, 'darkblue')

#moon
color('bisque')

pen_move(0, -133)
begin_fill()
circle(180)
end_fill()


for i in range(9): 
    x_stein=randint(-130,130)
    y_stein=randint(-130,140)
    r_stein= randint(10,50) 
    stein(x_stein,y_stein,r_stein)


#builds
x=-250 
for i in range(17):
    weight = 30 + randint(5,15)
    height = 200 + randint(-80,80)
    build (x, -240, weight , height, 'black' )
    window(randint(x, int(x+weight/2)), randint(-240, -240+int(height/2)-10), 4, 10, 'yellow')
    window(randint(x, int(x+weight/2)), randint(-240+int(height/2), -240+height-10), 4, 10, 'yellow')
    x+=30


exitonclick()
hideturtle()
