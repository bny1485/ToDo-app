
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(FlaskForm):
    user_name = StringField('username', validators=[DataRequired(), Length(min=5, max=32, message='Your username must be at least 5 words and at most 32 words')])
    email = StringField('Email addrese', validators=[DataRequired(), Email()])
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email addrese', validators=[DataRequired(), Email()])
    password = PasswordField('Password')
    submit = SubmitField('Sign In')
