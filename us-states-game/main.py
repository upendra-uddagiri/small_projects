import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
states = data.copy()
guessed_state=[]
count = 0

while count < 50:
    answer = screen.textinput(
        f"{count}/50 States Correct",
        "What's another state name?"
    )

    if answer is None:   # user pressed Cancel
        break

    answer = answer.title()
    if answer=="Exit":
        break
    state_data = states[states["state"] == answer]

    if not state_data.empty:
        count += 1
        guessed_state.append(answer)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()

        x = int(state_data.x)
        y = int(state_data.y)
        writer.goto(x, y)
        writer.write(answer)

        states = states[states["state"] != answer]

