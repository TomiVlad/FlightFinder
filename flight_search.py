import requests
import pprint
import os
from flight_data import FlightData

API_KEY = os.getenv("Tequilla_API_KEY")
TEQUILLA_ENDPOINT = "https://api.tequila.kiwi.com"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILLA_ENDPOINT}/locations/query"
        headers = {"apikey": API_KEY}
        query = {
            "term": city_name,
            "location_types": "airport",
        }
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        response_data = response.json()["locations"]
        return response_data[0]["id"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 10,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "RON"
        }

        response = requests.get(
            url=f"{TEQUILLA_ENDPOINT}/v2/search",
            headers = headers,
            params = query
            )


        try:
            data = response.json()["data"][0]

        except IndexError:
            # Change the allowed stosps.
            query["max_stopovers"] = 2

            # Search again for a flight.
            response = requests.get(
            url=f"{TEQUILLA_ENDPOINT}/v2/search",
            headers = headers,
            params = query
            )

            # Keep the data in a variable called "data".
            data = response.json()["data"][0]

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )

        else:

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )

            return flight_data
