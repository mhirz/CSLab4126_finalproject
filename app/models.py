from app import app
from flask_login import UserMixin

class User(UserMixin):

    # Dave please implement how users are saved to DB

    def __init__(self, surename, lastname, email, password,):
        self.surename = surename
        self.lastname = lastname
        self.email = email
        self.password = password

    def __repr__(self):
        return ''%self.username