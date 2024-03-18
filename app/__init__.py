from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'NBA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nba.db'
db = SQLAlchemy(app)

from app import routes
