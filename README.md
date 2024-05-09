Flight Price Tracker Program
Description:
This program is designed to find the cheapest flights available within a 6-month timeframe for a maximum duration of 7 days. 
If flight prices below a specified target are discovered, the program will automatically send an email notification to the user-provided email address.

Features:
- Utilizes the Kiwi API for flight searches.
- Stores destination and price information in a Google Sheet database format.
- Retrieves data from the database using the Sheety API.
- Sends email notifications using the smtplib library.

Installation:
- Clone the repository to your local machine.
- Install the required dependencies by running pip install -r requirements.txt.
- Obtain API keys for Kiwi and Sheety and update the corresponding variables in the program.
- Run the program.
  
Usage:
- Provide the desired search criteria, including departure and destination locations, date range, and price target.
- Run the program.
- eceive email notifications if flights meeting the criteria are found.
