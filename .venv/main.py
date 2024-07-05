# Turtle race program!

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput(title="Bet", prompt="Who is going to win?")
print(bet)


colors = ["blue", "red", "orange", "green", "purple", "yellow"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_positions[turtle_index])
    turtles.append(new_turtle)



race_is_on = False
if bet:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You win! {winner} is the winner!")
            else:
                print(f"You lose. {winner} is the winner")
        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()