#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from ask_user import AskUser, UserInfo
import sheety

def calculate_six_months_period():
    # Get the current date
    current_date = datetime.now()

    # Calculate the end date by adding 6 months
    end_date = current_date + timedelta(days=180)

    # Format dates as strings with the desired format (dd/mm/yyyy)
    current_date_str = current_date.strftime("%d/%m/%Y")
    tomorrow = current_date + timedelta(days=1)
    tomorrow = tomorrow.strftime("%d/%m/%Y")
    end_date_str = end_date.strftime("%d/%m/%Y")

    return current_date_str, tomorrow, end_date_str

def get_info_from_the_user():
    print("Welcome to Flight Club.\n \
    We find the best flight deals and email them to you.")

    first_name = input("What is your first name? \n").title()
    last_name = input("What is your last name? \n").title()

    email_1 = "email_1"
    email_2 = "email_2"

    while email_1 != email_2:
        email_1 = input("What is your email?\n")
        if email_1.lower() == "quit" or email_1.lower() == "exit":
            exit()

        email_2 = input("Please verify your email : \n")
        if email_2.lower() == "quit" or email_2.lower() == "exit":
            exit()

    print("You are in the club!")

    sheety.post_new_row(first_name, last_name, email_1)

# Create the DataManager object.
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
user_info = AskUser()

# Ask user for the details.
get_info_from_the_user()

# The starting point of the trip.
ORIGIN_CITY_IATA = ["CLJ"]

if sheet_data[0]['iataCode'] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

current_day, tomorrow, six_month_from_today = calculate_six_months_period()
msg = ""

for orig_city_iata in ORIGIN_CITY_IATA:
    for destination in sheet_data:
        flight = flight_search.check_flights(
        orig_city_iata,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
        )


        if flight is None:
            continue
        else:
            if flight.price < destination["lowestPrice"]:
                msg = (
                        msg
                        + f"Low price alert! Only {flight.price} RON to fly from "
                        f"{flight.origin_city}-{flight.origin_airport} to "
                        f"{flight.destination_city}-{flight.destination_airport}, from "
                        f"{flight.out_date} to {flight.return_date}.\n"
                    )

                if flight.stop_overs > 0:
                    message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
                    print(message)

users_data = data_manager.get_user_data()


notification_manager.send_email(
    message= msg,
    users_dict=users_data
)

