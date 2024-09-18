from turtle import Turtle
import random


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color('#e6a020')
        self.speed('fastest')
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 380)
        self.goto(x=random_x, y=random_y)
        
    def refesh(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 380)
        self.goto(x=random_x, y=random_y)