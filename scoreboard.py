from turtle import Turtle
FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=368)
        self.score = 0
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
        
    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(x=0, y=0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT )