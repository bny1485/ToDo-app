
from flask import Flask
from utils import random_string
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = random_string
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "users.login"
login_manager.login_message_category = 'info'


from users.routes import users
from main.routes import main
app.register_blueprint(main)
app.register_blueprint(users)


if __name__ == "__main__":
    app.run(debug=True)
