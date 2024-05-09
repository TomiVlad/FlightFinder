import requests
import os


BEARER = os.getenv("API_Bearer_Sheety_Repl.it")
USERNAME = os.getenv("API_Username_Sheety")

PROJECT = "flightDeals"
SHEET_PRICES = "prices"
SHEET_USERS = "users"

base_url = "https://api.sheety.co"

endpoint_url_prices = f"/{USERNAME}/{PROJECT}/{SHEET_PRICES}"
endpoint_url_users = f"/{USERNAME}/{PROJECT}/{SHEET_USERS}"
SHETTY_PRICES_ENDPOINT = base_url + endpoint_url_prices
SHETTY_USERS_ENDPOINT = base_url + endpoint_url_users

headers = {
    "Authorization": f"Bearer {BEARER}",
    "Content-Type": "application/json",
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}
        self.users_data = {}


    def get_destination_data(self):
        # Use Shetty API to get all the data from that sheet and print it out.
        response = requests.get(url=SHETTY_PRICES_ENDPOINT, headers=headers)

        data = response.json()
        self.destination_data = data['prices']

        return self.destination_data


    def update_destination_data(self):

        for city in self.destination_data:
            new_data = {
                 "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHETTY_PRICES_ENDPOINT}/{city['id']}",
                headers=headers,
                json=new_data
            )

    def get_user_data(self):
        # Use Shetty API to get all the data from that sheet and print it out.
        response = requests.get(url=SHETTY_USERS_ENDPOINT, headers=headers)

        data = response.json()
        self.users_data = data['users']

        return self.users_data

