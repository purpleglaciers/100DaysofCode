import requests
from datetime import datetime
import smtplib
import time as t

MY_EMAIL = youremail@mail.com
MY_PASSWORD = your app password
sender = "'your name'\n-ISS Alerts"

MY_LAT = 33.448376
MY_LONG = -112.074036

print(f"My cords: {MY_LAT}, {MY_LONG}")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


# TODO 1: Your position is within +5 or -5 degrees of the ISS position.
def iss_overhead():
    global MY_LAT, MY_LONG
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"ISS cords: {iss_latitude}, {iss_longitude}")

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        return True


def is_night():
    global parameters
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    data = response.json()
    sunrise = (int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 7)
    sunset = (int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 17)
    time_now = datetime.now()
    print(f"sunrise: {sunrise}\nsunset: {sunset}\ntime now(hour): {time_now.hour}")
    if time_now.hour < sunrise or time_now.hour > sunset:
        return True


def email_alert():
    if iss_visible:
        global MY_EMAIL, MY_PASSWORD, sender
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="desired recipient",
                                msg="subject: Look up! The ISS is overhead!\n\n"
                                    f"The international Space Station (ISS) is currently visible in the sky above your "
                                    f"location.\n{sender}")
        print("Email alert sent")


# TODO 2: If the ISS is close to my current position and it is currently dark
while True:
    # TODO 4:(BONUS): run the code every 60 seconds.
    t.sleep(60)
    is_night()
    if iss_overhead() and is_night():
        # TODO 3: Then send me an email to tell me to look up.
        email_alert()
    else:
        print("ISS not currently visible overhead")
