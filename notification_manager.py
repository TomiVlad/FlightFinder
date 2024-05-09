import smtplib
import os

MY_EMAIL = os.getenv("Email_username")
PASSWORD = os.getenv("Email_password")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_email(self, message, users_dict):

        message = "Subject:" + "Bilete ieftine de avion" + "\n\n" + message

        email_list = []

        for user in users_dict:
            if 'email' in user:
                if user['email'] not in email_list:
                    email_list.append(user['email'])

        for user_email in email_list:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=user_email,
                        msg= message.encode("ascii","ignore")
                        )
            print(f"Email sent to: {user_email}\n")
