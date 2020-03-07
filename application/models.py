from application import db
from application import login_manager
from flask_login import UserMixin
from datetime import datetime

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
             'User ID: ', self.user_id, '\r\n',
             'Title: ', self.title, '\r\n', self.content
    ])


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])

class Leagues (db.Model):
    id = db.Column(db.Integer, primary_key =True)
    league_name = db.Column(db.String(40), nullable =False, unique = True)
    
    def __repr__(self):
        return f"Leagues('{self.league_name}' )"

class Club (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    club_name = db.Column(db.String(40), nullable = False, unique = False) 
    league_name = db.Column(db.String(40), nullable = False, unique = False )

    def __repr__(self):
        return f"Club('{self.club_name}', '{self.league_name}' )"

class Players (db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(40), nullable = False, unique = True)
    club_name = db.Column(db.String(40), nullable = False)
    league_name = db.Column(db.String(40), nullable = False)
    position = db.Column(db.String(20), unique=False, nullable=False)
    rating = db.Column(db.String(20), unique=False, nullable=False)
    
    def __repr__(self):
        return f"Players('{self.name}' , '{self.club_name}' , '{self.position}' , '{self.rating}' )"


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
