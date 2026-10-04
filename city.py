from turtle import *

def rect(x, y, weight, height, color_rect):
    color( color_rect)
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    for i in range(2):
        forward(weight)
        left(90)
        forward(height)
        left(90)
    end_fill()

        
