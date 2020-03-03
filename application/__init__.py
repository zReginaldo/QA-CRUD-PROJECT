from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://zReginaldoz:HelloWorld12@localhost/Flaskdb"
#app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config ['SECRET_KEY'] = "HelloWorld12"
#app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY'))
db = SQLAlchemy(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login'


from application import routes
