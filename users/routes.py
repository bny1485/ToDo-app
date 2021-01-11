from flask import Blueprint, render_template
from users.forms import RegistrationForm

users = Blueprint('users', __name__)

@users.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='register', form=form)
