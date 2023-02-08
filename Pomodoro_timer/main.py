import math
from tkinter import *
import time as t

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_tick = None



# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_tick)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps <= 7:
        reps += 1
    else:
        reps = 0
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer.config(text="Break", fg=YELLOW)
    else:
        countdown(work_sec)
        timer.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(number):
    count_minute = math.floor(number / 60)
    count_second = number % 60
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if number > 0:
        global timer_tick
        timer_tick = window.after(1000, countdown, number - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# TODO 1. Create tkinter window with bg color
window = Tk()
window.title("Pomodoro")
window.minsize(height=300, width=400)
window.config(padx=50, pady=40, bg=PINK)

timer = Label(text="TIMER", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=PINK)
timer.grid(row=0, column=1)
timer.config(pady=20)

#TODO 2. Create canvas
canvas = Canvas(width=200, height=223, bg=PINK, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 105, image=tomato_pic)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


#TODO 3. Create labels

check_mark = Label(fg=GREEN, bg=PINK)
check_mark.config(pady=15)
check_mark.grid(row=3, column=1)

# TODO 4. Creat start and reset buttons

start = Button(text="start", highlightbackground=PINK, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="reset", highlightbackground=PINK, command=reset_timer)
reset.grid(row=2, column=2)






window.mainloop()