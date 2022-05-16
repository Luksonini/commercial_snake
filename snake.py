import turtle
from turtle import Turtle
STARTING_POSITIONS = [0, -20, -40]
STEP_DISTANCE = 20
turtle.register_shape("./graphics/body2.gif", shape=None)
turtle.register_shape("./graphics/snhr.gif", shape=None)
turtle.register_shape("./graphics/snhl.gif", shape=None)
turtle.register_shape("./graphics/snhup.gif", shape=None)
turtle.register_shape("./graphics/snhd.gif", shape=None)

class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        self.snake_segments_number = 4
        self.new_segment = self.snake_segments[-1]


    def create_snake(self):
        for current_snake in range(1, 4):
            current_snake = Turtle()
            current_snake.shape('./graphics/body2.gif')
            current_snake.penup()
            self.snake_segments.append(current_snake)
        self.snake_segments[0].shape('./graphics/snhr.gif')


        for square_x, snake in enumerate(self.snake_segments):
            snake.goto(x=STARTING_POSITIONS[square_x], y=0)

    def add_segment(self):
        self.snake_segments_number += 1
        new_segment = Turtle()
        new_segment.hideturtle()
        new_segment.shape('./graphics/body2.gif')
        new_segment.speed("fastest")
        new_segment.penup()
        self.snake_segments.append(new_segment)


    def move(self):
        for index in range(len(self.snake_segments) - 1, 0, -1):
            previous_pos = self.snake_segments[index - 1].pos()
            self.snake_segments[index].goto(previous_pos)
            self.snake_segments[index].showturtle()
        self.head.forward(STEP_DISTANCE)

        if self.head.xcor() >= 300 or self.head.xcor() <= -300:
            loop_x_coordinate = self.head.xcor() * (-1)
            self.head.setx(loop_x_coordinate)

        elif self.head.ycor() >= 300 or self.head.ycor() <= -300:
            loop_y_coordinate = self.head.ycor() * (-1)
            self.head.sety(loop_y_coordinate)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
            self.snake_segments[0].shape('./graphics/snhup.gif')

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            self.snake_segments[0].shape('./graphics/snhd.gif')

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            self.snake_segments[0].shape('./graphics/snhl.gif')
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            self.snake_segments[0].shape('./graphics/snhr.gif')

    def clear(self):
        self.clear()