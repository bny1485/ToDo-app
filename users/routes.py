""" this is route file """
from flask import Blueprint, render_template, redirect, url_for
from users.forms import RegistrationForm, LoginForm
from run import db, bcrypt
from models import User
from flask_login import login_user, current_user


users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    ''' this function register user and if user was login user can not come to this page '''
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(user_name=form.user_name.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('register.html', title='register', form=form)



@users.route('/login', methods=['POST', 'GET'])
def login():
    ''' log in users to there account '''
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=False)
            return redirect(url_for('main.home'))
    return render_template('login.html', title='login', form=form)