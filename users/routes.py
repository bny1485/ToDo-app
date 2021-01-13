from flask import Blueprint, render_template
from users.forms import RegistrationForm, LoginForm


users = Blueprint('users', __name__)


@users.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='register', form=form)


@users.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)
