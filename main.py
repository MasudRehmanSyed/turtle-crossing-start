import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('grey')
screen.tracer(0)
# Create player, scoreboard and cars
player = Player()
score = Scoreboard()
car_manager = CarManager()
car_manager.create_car()

screen.onkey(player.go_up, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # check for collisions
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
    if player.ycor() > 280:
        score.level_up()
        player.won()
        car_manager.speed_up()

score.game_over()
screen.exitonclick()
