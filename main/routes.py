from flask import Blueprint, render_template


main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    return render_template('main.html',title='home')
