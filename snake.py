from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    
    def __init__(self):
        self.snake_parts = []
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def move(self):
        for snake_part_number in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[snake_part_number-1].xcor()
            new_y = self.snake_parts[snake_part_number-1].ycor()
            self.snake_parts[snake_part_number].goto(x=new_x, y=new_y)
        self.snake_parts[0].forward(MOVE_DISTANCE)
        
    def add_segment(self, position):
        self.snake_part = Turtle(shape='square')
        self.snake_part.color('#67bd4f')
        self.snake_part.penup()
        self.snake_part.goto(position)
        self.snake_parts.append(self.snake_part)
    
    def extend(self):
        self.add_segment(self.snake_parts[-1].position())
        
    def up(self):
        if self.snake_parts[0].heading() != DOWN:
            self.snake_parts[0].setheading(UP)

    def down(self):
        if self.snake_parts[0].heading() != UP:
            self.snake_parts[0].setheading(DOWN)
    
    def left(self):
        if self.snake_parts[0].heading() != RIGHT:
            self.snake_parts[0].setheading(LEFT)
    
    def right(self):
        if self.snake_parts[0].heading() != LEFT:
            self.snake_parts[0].setheading(RIGHT)