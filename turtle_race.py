from turtle import Turtle
from random import randint

laura = Turtle()
rick = Turtle()
lauren= Turtle()
joe = Turtle()

laura.color('red')
laura.shape('turtle')
laura.penup()
laura.goto(-160,100)
laura.pendown()

rick.color('blue')
rick.shape('turtle')
rick.penup()
rick.goto(-160,70)
rick.pendown()

for movememnt in range(100):
    laura.forward(randint(1,5))
    rick.forward(randint(1,5))
    
input("Press Enter to close")