from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.sety(260)
        self.color('white')
        self.current_score = 0
        self.renew_scoreboard()

    def renew_scoreboard(self):
        self.write(f"earned coupons: {self.current_score}", align='center', font=('Garamond', 25, 'bold'))

    def restart_score(self):
        self.sety(260)
        self.color('white')
        self.current_score = 0
        self.clear()
        self.renew_scoreboard()


    def new_point(self):
        self.current_score +=1
        self.clear()
        self.renew_scoreboard()

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 50)
        self.color('red')
        self.write(f"GAME OVER", align='center', font=('Garamond', 25, 'bold'))

    def you_won(self, level):
        self.level = level
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.color('red')
        if self.level == 1:
            text = '''You have won the Big Mac!'''
        elif self.level == 2:
            text = '''
  You have won the 
     KFC bucket! '''
        elif self.level == 3:
            text = '''You have won the Pizza! '''
        self.write(text, align='center', font=('Garamond', 35, 'bold'))








