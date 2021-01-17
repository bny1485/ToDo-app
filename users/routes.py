""" this is route file """
from flask import Blueprint, render_template, redirect, url_for
from users.forms import RegistrationForm, LoginForm
from run import db, bcrypt
from models import User


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


