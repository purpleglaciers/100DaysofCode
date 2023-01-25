from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Type a color: ")
print(f"You chose {user_bet}. Starting race...")

colors = ["red", "blue", "yellow", "purple", "green", "orange"]
all_turtles = []


def starting_positions(y_value):
    for turtle_index in range(len(colors)):
        new_turtle = Turtle()
        new_turtle.color(colors[turtle_index])
        new_turtle.shape("turtle")
        if colors[turtle_index] == "yellow":
            new_turtle.color("black", "yellow")
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_value)
        all_turtles.append(new_turtle)

        y_value -= 25


starting_positions(75)


def finish_line():
    finish_line_turtle = Turtle()
    finish_line_turtle.penup()
    finish_line_turtle.goto(x=230, y=200)
    finish_line_turtle.pendown()
    finish_line_turtle.setheading(270)
    finish_line_turtle.forward(400)
    finish_line_turtle.hideturtle()


finish_line()


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 220:
            is_race_on = False
            if turtle.fillcolor == user_bet:
                print(f"{turtle.fillcolor()} wins the race. You win the bet!")
            else:
                print(f"{turtle.fillcolor()} wins. You lose the bet.")


screen.exitonclick()
