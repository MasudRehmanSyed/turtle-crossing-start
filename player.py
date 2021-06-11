from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')

        self.seth(90)
        self.pu()
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def won(self):
        self.goto(STARTING_POSITION)
