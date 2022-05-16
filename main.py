import turtle
from turtle import Screen
from snake import Snake
from food import Food
from poo import Poo, poo_list
from scoreboard import Scoreboard
import pygame
pygame.init()
pygame.mixer.init()
import time



screen = Screen()
scoreboard = Scoreboard()


def coupons_to_win(level):
    if level == 1:
        return 7
    elif level == 2:
        return 8
    elif level == 3:
        return 9
    elif level == 4:
        return 9999

def background(level):
    if level == 1:
        screen.bgpic("./graphics/mac2.gif")
    elif level == 2 or level == 4:
        screen.bgpic("./graphics/kfc.gif")
    elif level == 3:
        screen.bgpic("./graphics/pizza_bg.gif")


def chooce_winnin_gscreen(level):
    if level == 1:
        screen.bgpic("./graphics/big_mac.gif")
        scoreboard.you_won(level)
        level_sound = pygame.mixer.Sound('./sounds/parapapa.wav')
        level_sound.play()
    elif level == 2 or level == 4:
        screen.bgpic("./graphics/chicken.gif")
        scoreboard.you_won(level)
        level_sound = pygame.mixer.Sound('./sounds/aplause.wav')
        level_sound.play()
    elif level == 3:
        screen.bgpic("./graphics/pizza_won.gif")
        scoreboard.you_won(level)
        level_sound = pygame.mixer.Sound('./sounds/pizza_sound.wav')
        level_sound.play()



def game():
    while True:  # Pętla umożliwiająca restart gry
        for level in range(1, 5):
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

            while game_on:
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
                    food_sound = pygame.mixer.Sound('./sounds/food_sound.wav')
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
                        loose_sound = pygame.mixer.Sound("./sounds/loose_sound.wav")
                        loose_sound.play()
                        scoreboard.game_over()
                        restart = screen.textinput("a", "Do you want to restart ? (y/n)")
                        if restart == "y":
                            poo.restart()
                            screen.clearscreen()
                            scoreboard.restart_score()
                            break  # Wyjście z pętli 'for', powrót do początku pętli 'while'
                        else:
                            return  # Zakończenie gry

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
                            break  # Wyjście z pętli 'for', powrót do początku pętli 'while'
                        else:
                            return  # Zakończenie gry

                # terms of winning
                if len(snake.snake_segments) > coupons_to_win(level):
                    screen.clearscreen()
                    chooce_winnin_gscreen(level)
                    poo.restart()
                    scoreboard.restart_score()
                    break  # Wyjście z pętli 'for', powrót do początku pętli 'while'

# Wywołanie funkcji game
game()



