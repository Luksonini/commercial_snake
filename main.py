
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from poo import Poo, poo_list
from scoreboard import Scoreboard
import pygame
import time
import sys
import os

# Initialize Pygame and its mixer module for sound handling
pygame.init()
pygame.mixer.init()


def resource_path(relative_path):
    """ Get absolute path to resource, works for development and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Setting up the game screen
screen = Screen()
scoreboard = Scoreboard()

# Function defining the number of points required to win at each level
def coupons_to_win(level):
    # Logical conditions for different levels
    if level == 1:
        return 7
    elif level == 2:
        return 8
    elif level == 3:
        return 9
    elif level == 4:
        return 9999

# Function to set the background based on the level
def background(level):
    # Set the appropriate background for each level using the resource_path function
    if level == 1:
        screen.bgpic(resource_path("graphics/mac2.gif"))
    elif level == 2 or level == 4:
        screen.bgpic(resource_path("graphics/kfc.gif"))
    elif level == 3:
        screen.bgpic(resource_path("graphics/pizza_bg.gif"))

# Function handling the winning screen display
def chooce_winnin_gscreen(level):
    # Display the correct winning screen based on the level using the resource_path function
    if level == 1:
        screen.bgpic(resource_path("graphics/big_mac.gif"))
        scoreboard.you_won(level)
        level_sound = pygame.mixer.Sound(resource_path('sounds/parapapa.wav'))
        level_sound.play()
    elif level == 2 or level == 4:
        screen.bgpic(resource_path("graphics/chicken.gif"))
        scoreboard.you_won(level)
        level_sound = pygame.mixer.Sound(resource_path('sounds/aplause.wav'))
        level_sound.play()
    elif level == 3:
        screen.bgpic(resource_path("graphics/pizza_won.gif"))
        scoreboard.you_won(level)
        level_sound = pygame.mixer.Sound(resource_path('sounds/pizza_sound.wav'))
        level_sound.play()


# Main game function
def game():
    # Loop to allow for game restart
    while True:  
        # Loop for each level of the game
        for level in range(1, 5):
            # Specific conditions for each level
            if level == 4:
                restart = screen.textinput("a", "Do you want to try infinite mode? (y/n)")
                if restart != "y":
                    return
            start_time = time.time()
            game_on = True
            ELAPSED_TIME = 10
            screen.setup(width=600, height=600)
            screen.title("Snake Game")
            screen.tracer(0)
            snake = Snake()
            food = Food()
            food.new_food(level)
            screen.listen()
            screen.onkey(snake.up, "Up")
            screen.onkey(snake.down, "Down")
            screen.onkey(snake.left, "Left")
            screen.onkey(snake.right, "Right")

            # Main game loop
            while game_on:
                # Updating background, moving the snake, checking for collisions, etc.
                background(level)
                screen.update()
                time.sleep(0.1)
                snake.move()
                poo_pos_x = snake.snake_segments[-1].xcor()
                poo_pos_y = snake.snake_segments[-1].ycor()
                poo = Poo(poo_pos_x, poo_pos_y)

                # food interaction
                if food.distance(snake.head) < 25:
                    food.new_food(level)
                    scoreboard.new_point()
                    snake.add_segment()
                    food_sound = pygame.mixer.Sound(resource_path('sounds/food_sound.wav'))
                    food_sound.play()
                    poo.make_poo()
                    start_time = time.time()

                # food restart
                elapsed_time = time.time() - start_time
                if elapsed_time > ELAPSED_TIME:
                    start_time = time.time()
                    food.new_food(level)

                # poo collision
                for element in poo_list:
                    if element.distance(snake.head) < 25:
                        game_on = False
                        loose_sound = pygame.mixer.Sound(resource_path("./sounds/loose_sound.wav"))
                        loose_sound.play()
                        scoreboard.game_over()
                        restart = screen.textinput("a", "Do you want to restart ? (y/n)")
                        if restart == "y":
                            poo.restart()
                            screen.clearscreen()
                            scoreboard.restart_score()
                            break 
                        else:
                            return  

                # snake self collision
                for segment in snake.snake_segments[1:]:
                    if snake.head.distance(segment) < 10:
                        game_on = False
                        loose_sound = pygame.mixer.Sound("./sounds/loose_sound.wav")
                        loose_sound.play()
                        restart = screen.textinput("a", "Do you want to restart ? (y/n)")
                        if restart == "y":
                            poo.restart()
                            screen.clearscreen()
                            scoreboard.restart_score()
                            break  
                        else:
                            return 

                # terms of winning
                if len(snake.snake_segments) > coupons_to_win(level):
                    screen.clearscreen()
                    chooce_winnin_gscreen(level)
                    poo.restart()
                    scoreboard.restart_score()
                    break  


game()



