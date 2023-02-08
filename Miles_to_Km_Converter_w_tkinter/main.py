from tkinter import *
import pandas


data_list = ["log"]
conv_data = pandas.DataFrame(data_list)

# TODO 6. Build function that activates on button click and initiates the calculation

def button_clicked():
    with open("recent_conversion_log.csv", "r") as file:
        data_list = [file.read()]
    results.config(text=round((float(miles_input.get()) * 1.6), 2))
    data_list.append(f"converted {miles_input.get()} miles into {round((float(miles_input.get()) * 1.6), 2)} Km")
    conv_data = pandas.DataFrame(data_list)
    conv_data.to_csv("recent_conversion_log.csv")
# TODO 7. Append data from current calculation to list, and write current list to csv

    if conv_data.shape[0] >= 11:
        data_list.pop(10)

# TODO 1. Create the tkinter window and adjust size and title
window = Tk()
window.minsize(width=200, height=200)
window.config(padx=50, pady=30)
window.title("Mile to Km Converter")


# TODO 2. Create calculate button and grid it
calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(column=1, row=2)
calc_button.config(padx=10)

#TODO 3. Create 'Miles', 'is equal to', 'result', and 'Km' labels and grid them
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

results = Label(text=0)
results.grid(column=1, row=1)
results.config(pady=10)


#TODO 4. Create Miles entry and grid it
miles_input = Entry(width=12)
miles_input.grid(column=1, row=0)



window.mainloop()
