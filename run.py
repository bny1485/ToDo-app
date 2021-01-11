
from flask import Flask
from main.routes import main
from users.routes import users
from utils import random_string



app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(users)

app.config['SECRET_KEY'] =  random_string

if __name__ == "__main__":
    app.run(debug=True)
