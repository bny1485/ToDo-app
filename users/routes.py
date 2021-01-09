from flask import Blueprint, render_template

users = Blueprint('users', __name__)

@users.route('/register')
def register():
    return render_template('register.html', title='register')
