
from flask import Flask
from utils import random_string
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = random_string
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)



from users.routes import users
from main.routes import main
app.register_blueprint(main)
app.register_blueprint(users)


if __name__ == "__main__":
    app.run(debug=True)
