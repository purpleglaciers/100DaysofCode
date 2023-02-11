from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    add_letters = [choice(letters) for _ in range(randint(8, 10))]
    add_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    add_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = add_letters + add_symbols + add_numbers
    shuffle(password_list)

    password = "".join(password_list)
    for char in password_list:
        password += char

    enter_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = enter_website.get()
    email = enter_email.get()
    password = enter_password.get()
    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Oops! Don't leave any boxes empty!")
    else:
        is_ok = messagebox.askokcancel(title="Confirm Password", message=f"You entered:\nWebsite: {website}\n"
                                f"Email: {email}\nPassword: {password}\nWould you like to save this password?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                enter_website.delete(0, END)
                enter_email.delete(0, END)
                enter_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Awesome Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website = Label(text="Website:", font=("Ariel", 13, "normal"))
website.grid(row=1, column=0)

email_username = Label(text="Email/Username:", font=("Ariel", 13, "normal"))
email_username.grid(row=2, column=0)

password = Label(text="Password:", font=("Ariel", 13, "normal"))
password.grid(row=3, column=0)

generate = Button(text="Generate Password", width=13, font=("Arial", 11, "normal"), command=generate_password)
generate.grid(row=3, column=2)

enter_website = Entry(width=35)
enter_website.grid(row=1, column=1, columnspan=2)
enter_website.insert(0, "Hbo Max")

enter_email = Entry(width=35)
enter_email.grid(row=2, column=1, columnspan=2)
enter_email.insert(0, "john@mailbox.com")

enter_password = Entry(width=21)
enter_password.grid(row=3, column=1)

add = Button(text="Add", font=("Ariel", 13, "normal"), width=33, command=save_data)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
