import datetime as dt
import random
import smtplib
import pandas

my_email = your_gmail_address
my_password = your_app_password
sender = your_name


#TODO 1. Update the birthdays.csv with friends & family's details.

#TODO 3. Send the email
def send_letter(name, email):
    global my_email, my_password, person, sender
    letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    with open(random.choice(letters), "r") as file:
        text = file.read().replace("[NAME]", name).replace("Angela", sender)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email,
                                msg=f"Subject:Happy Bday!\n\n{text}"
                                )


#TODO 2. Check if today matches a birthday in the birthdays.csv
birthdays = open("birthdays.csv", "r")
df = pandas.read_csv("birthdays.csv")
data = df.to_dict("records")

today = dt.datetime.now()

for person in data:
    if person["month"] == today.month and person["day"] == today.day:
        send_letter(person["name"], person["email"])

