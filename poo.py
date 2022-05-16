from turtle import Turtle
import turtle
turtle.register_shape("./graphics/poo.gif", shape=None)
poo_list = []

class Poo():
    def __init__(self, initial_pos_x, initial_pos_y):
        self.initial_pos_x = initial_pos_x
        self.initial_pos_y = initial_pos_y



    def make_poo(self):
        self.current_poo = Turtle('./graphics/poo.gif')
        self.current_poo.penup()
        self.current_poo.goto(self.initial_pos_x, self.initial_pos_y)
        poo_list.append(self.current_poo)

    def restart(self):
        poo_list.clear()




