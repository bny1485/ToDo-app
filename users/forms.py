
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from models import User


class RegistrationForm(FlaskForm):
    user_name = StringField('username', validators=[DataRequired(), Length(min=2, max=32)])
    email = StringField('Email addrese', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm-Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, user_name):
        user = User.query.filter_by(user_name=user_name.data).first()
        if user:
            raise ValidationError('User is alredy exist')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email is alredy exist')

class LoginForm(FlaskForm):
    email = StringField('Email addrese', validators=[DataRequired(), Email()])
    password = PasswordField('Password')
    submit = SubmitField('Sign In')
