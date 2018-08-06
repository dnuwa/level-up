import re

class Signup():
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = Signup.validate_email(email_address)
        self.database= []

    def combined_name(self):
        print(self.first_name+" " + self.last_name)

    def submit(self):
        self.users = {'first_name': self.first_name,
                      'last_name': self.last_name, 'email': self.email_address}
        self.database.append(self.users)
        print(self.database)


    @staticmethod
    def validate_email(email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        else:
            return email


new_user = Signup("bulega", "godfrey", "bulega@gmail.com")
new_user.combined_name()
new_user.submit()
