from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users
from flask_login import current_user



class LeaguesForm(FlaskForm):
    leagues = SelectField ('leagues', choices=[('England Premier League', 'English Premier League'), ('France Ligue 1', 'French League'), ('Germany 1. Bundesliga','Bundesliga'),('Italy Serie A','Serie A'),('Spain Primera Division', 'Spanish League')])
    club = SelectField ('club', choices=[])
    players = SelectField ('players', choices=[])



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
