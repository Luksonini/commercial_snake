import turtle
from turtle import Turtle
import random
import time
turtle.register_shape("./graphics/burger2.gif", shape=None)
turtle.register_shape("./graphics/legs.gif", shape=None)
turtle.register_shape("./graphics/pizza_piece.gif", shape=None)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")



    def new_food(self, level):
        self.level = level
        if self.level == 1:
            self.shape("./graphics/burger2.gif")
        elif self.level == 2 or self.level == 4:
            self.shape("./graphics/legs.gif")
        elif self.level == 3:
            self.shape("./graphics/pizza_piece.gif")
        self.hideturtle()
        self.goto(x=random.randint(-270, 270), y=random.randint(-270, 270))
        self.showturtle()

