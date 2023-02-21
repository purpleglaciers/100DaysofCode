import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Swedish top 100 frequency words - Sheet1.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")


def new_card():
    global current_card, flip_timer, to_learn
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card)
    canvas.itemconfig(lang, text="Swedish", fill="black")
    canvas.itemconfig(word, text=current_card["Swedish"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card, to_learn
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def is_known():
    global current_card, to_learn
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    print(len(data))
    new_card()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=card_front)
lang = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

card_back = PhotoImage(file="images/card_back.png")

check_image = PhotoImage(file="images/right.png")
check_mark = Button(image=check_image, highlightbackground=BACKGROUND_COLOR, command=is_known)
check_mark.grid(row=1, column=1)

x_image = PhotoImage(file="images/wrong.png")
x_mark = Button(image=x_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=new_card)
x_mark.config(borderwidth=0)
x_mark.grid(row=1, column=0)


new_card()

window.mainloop()
