import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image_of_US = "blank_states_img.gif"
screen.addshape(image_of_US)

turtle.shape(image_of_US)


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

# call the correctly guessed state's info as dictionary, so we can easily grab the coordinates and state name from it.

while len(guessed_states) < 50:
    user_guess = screen.textinput("Guess the state", "Type the name of a state to guess:")
    if user_guess == "Exit":
        break
    if user_guess in states:
        guessed_states.append(user_guess)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = data[data.state == user_guess]
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(f"{user_guess}", font=("Courier", 9, "normal"))

states_to_learn = [state for state in states if state not in guessed_states]
open("states_to_learn.csv", "w")
states_to_learn_df = pandas.DataFrame(states_to_learn)
states_to_learn_df.to_csv("states_to_learn.csv")






















