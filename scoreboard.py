from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.ht()
        self.pu()
        self.goto(-220, 220)
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f'LEVEL {self.level} ', align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.display_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER! ', align='center', font=FONT)
