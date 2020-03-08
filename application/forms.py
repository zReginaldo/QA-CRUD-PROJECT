from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import *
from flask_login import current_user


class LeaguesForm(FlaskForm):

    leagues = SelectField ('leagues', choices=[('England Premier League', 'English Premier League'), ('France Ligue 1', 'French League'), ('Germany 1. Bundesliga','Bundesliga'),('Italy Serie A','Serie A'),('Spain Primera Division', 'Spanish League')])
    club = SelectField ('club', choices=[])
    players = SelectField ('Selection: 1', choices=[])
    
    leagues1 = SelectField ('leagues1', choices=[('England Premier League', 'English Premier League'), ('France Ligue 1', 'French League'), ('Germany 1. Bundesliga','Bundesliga'),('Italy Serie A','Serie A'),('Spain Primera Division', 'Spanish League')])
    club1 = SelectField ('club1', choices=[])
    players1 = SelectField ('Selection: 2', choices=[])
    
    
    leagues2 = SelectField ('leagues2', choices=[('England Premier League', 'English Premier League'), ('France Ligue 1', 'French League'), ('Germany 1. Bundesliga','Bundesliga'),('Italy Serie A','Serie A'),('Spain Primera Division', 'Spanish League')])
    club2 = SelectField ('club2', choices=[])
    players2 = SelectField ('Selection: 3', choices=[])
    
    
    leagues3 = SelectField ('leagues3', choices=[('England Premier League', 'English Premier League'), ('France Ligue 1', 'French League'), ('Germany 1. Bundesliga','Bundesliga'),('Italy Serie A','Serie A'),('Spain Primera Division', 'Spanish League')])
    club3 = SelectField ('club3', choices=[])
    players3 = SelectField ('Selection: 4', choices=[])
    
    
    leagues4 = SelectField ('leagues4', choices=[('England Premier League', 'English Premier League'), ('France Ligue 1', 'French League'), ('Germany 1. Bundesliga','Bundesliga'),('Italy Serie A','Serie A'),('Spain Primera Division', 'Spanish League')])
    club4 = SelectField ('club4', choices=[])
    players4 = SelectField ('Selection: 5', choices=[])

    submit = SubmitField('Confirm Team Selection')

    """

    def validate_players(self,players):
        playersq = Players.query.filter_by(name=players.data).first() 
        if playersq:
            return("Correct")
        else:
            raise ValidationError('Ensure Fields Arent Empty')

    def validate_players1(self,players1):
        playersq1 = Players.query.filter_by(name=players1.data).first()
        if playersq1:
            return("Correct")
        else:
            raise ValidationError('Ensure Fields Arent Empty')

    def validate_players2(self,players2):
        playersq2 = Players.query.filter_by(name=players2.data).first()
        if playersq2:
            return("Correct")
        else:
            raise ValidationError('Ensure Fields Arent Empty')

    def validate_players3(self,players3):
        playersq3 = Players.query.filter_by(name=players3.data).first()
        if playersq3:
            return("Correct")
        else:
            raise ValidationError('Ensure Fields Arent Empty')
    
    def validate_players4(self,players4):
        playersq4 = Players.query.filter_by(name=players4.data).first()
        if playersq4:
            return("Correct")
        else:
            raise ValidationError('Ensure Fields Arent Empty')

        """




class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')

class PostForm(FlaskForm):
        title = StringField('Title',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
        content = StringField('Content',
        validators = [
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )
        submit = SubmitField('Post!')


class RegistrationForm(FlaskForm):
        first_name = StringField('First Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
        last_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )

        email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
        password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
        confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
        submit = SubmitField('Sign Up')

        def validate_email(self, email):
            user = Users.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
