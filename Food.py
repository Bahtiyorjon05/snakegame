from turtle import Turtle
import random
import time

class SpecialFood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=2.3, stretch_wid=2.3)  # Larger size
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        self.hideturtle()
        self.schedule_appearance()

    def refresh(self):

        random_x = random.randint(-375, 375)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)


    def appear(self):
        self.refresh()
        self.showturtle()
        self.getscreen().ontimer(self.disappear, 5000)  # Hide after 5 seconds

    def disappear(self):
        self.hideturtle()
        self.schedule_appearance()

    def schedule_appearance(self):
        self.getscreen().ontimer(self.appear, 30000)  # Appear every 30 seconds

    
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
       super().__init__()
       self.shape("circle")
       self.penup()
       self.shapesize(stretch_len=0.7, stretch_wid=0.7)
       self.color("yellow")
       self.speed("fastest")
       self.refresh()
    def refresh(self):
       random_x=random.randint(-375,375) 
       random_y=random.randint(-275,275)  
       self.goto(random_x, random_y)

    

