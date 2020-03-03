from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(20), unique=False, nullable=False)
    Last_name = db.Column(db.String(40), unique=False, nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)
    Password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n',
            'Email: ', self.Email], '\r\n',
            'Name: ', self.First_name, ' ', self.Last_name
            )


class Leauges (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    League_Name = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return f"Leagues('{self.League_Name}' )"



class Club (db.Model):
    id = db.Column(db.Interger,primary_key = True)
    Club_Name = db.Column(db.String(50), unique=False, nullable=False)

    def __repr__(self):
        return f"Club('{self.Club_Name}')"



class Players (db.Models):
    id = db.Column(db.Interger,primary_key = True)
    First_name = db.Column(db.String(20), unique=False, nullable=False)
    Last_name = db.Column(db.String(120), unique=False, nullable=False)
    Club_name = db.Column(db.String(20), unique=False, nullable=False)
    Position = db.Column(db.String(3), unique=False, nullable=False)
    Rating = db.Column(db.String(2), unique=False, nullable=False)

    def __repr__(self):
        return f"Players('{self.First_name}' , '{self.Last_name}' , '{Club_name}' , '{Position}' , '{Rating}' )"


