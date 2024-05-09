# Asking the user to introduce the first name, last name and the email adress twice.
# Also, checking if the email adresses are the same.

class UserInfo:
    def __init__(self, first_name, last_name, email_adress):
        self.first_name = first_name
        self.last_name = last_name
        self.email_adress = email_adress

class AskUser:
    def get_user_info(self):
        first_name = input("Welcome to the Flight Club!\nWhat is your first name?\n")
        last_name = input("What is your last name?\n")
        email_adress = input("What is your email?\n")
        email_check = input("Type your email again.\n")

        if email_adress == email_check:
            print("You are in the club!")
            user_info = UserInfo(first_name, last_name, email_adress)
        else:
            print("Email adresses are not the same!")
            exit()

        return user_info




