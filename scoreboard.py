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
        self.highscore = self.get_highscore()
        self.write(f'Score: {self.score}  Highscore: {self.highscore}', align=ALIGNMENT, font=FONT)
        
    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}  Highscore: {self.highscore}', align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(x=0, y=0)
        self.write('GAME OVER\nClick to exit', align=ALIGNMENT, font=FONT )
        if self.score > int(self.highscore):
            self.new_highscore()
        
    def get_highscore(self):
        with open('data.txt', 'r') as f:
            high_score = f.read()
        return high_score
    
    def new_highscore(self):
        with open('data.txt', 'w') as f:
            f.write(str(self.score))