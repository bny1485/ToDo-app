
from flask import Flask
from main.routes import main
from users.routes import users


app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(users)


if __name__ == "__main__":
    app.run(debug=True)
