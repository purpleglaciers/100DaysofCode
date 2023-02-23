import requests
import random
from tkinter import *


response = requests.get(url="https://type.fit/api/quotes")
data = response.json()



def get_quote():
    global data
    choice = random.choice(data)
    quote = choice["text"]
    if len(quote) < 75:
        author = choice["author"]
        canvas.itemconfig(quote_text, text=f'"{quote}"')
        canvas.itemconfig(author_text, text=f"- {author}")
    else:
        get_quote()


window = Tk()
window.title("Inspirational Quotes😌")
window.config(height=500, width=500, background="blue", padx=20, pady=30)

canvas = Canvas(height=500, width=500, background="blue", highlightthickness=0)
quote_text = canvas.create_text(250, 250, text="Click the button bellow for inspiration!", fill="white")
author_text = canvas.create_text(250, 285, text="", font=("Arial", 12, "italic"), fill="white")

canvas.grid(row=0, column=0, columnspan=2)

generate = Button(text="New Quote", font=("Helvetica", 16, "normal"), command=get_quote)
generate.grid(row=1, column=0, columnspan=2)

window.mainloop()
