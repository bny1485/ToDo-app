
from flask import Flask
from main.routes import main
from users.routes import users
from utils import random_string

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] =  random_string


app.register_blueprint(main)
app.register_blueprint(users)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)
