import re

class Signup():
    def __init__(self, first_name, last_name, email_address):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.email_address = Signup.validate_email(email_address)
        self.database= []

    def combined_name(self):
        if not (self.first_name and self.last_name):
            return {'response':'first name and last name fields can not be empty'}
        else:
            return {self.first_name+" " + self.last_name}

    def submit(self):
        if not (self.first_name and self.last_name):
            return {'response':'first name and last name fields can not be empty'}
        else:
            self.users = {'first_name': self.first_name,
                        'last_name': self.last_name, 'email': self.email_address}
            self.database.append(self.users)
            return self.database


    @staticmethod
    def validate_email(email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        else:
            return email


new_user = Signup("", "", "bulega@gmail.com")
new_user.combined_name()
new_user.submit()
