
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class Todo(FlaskForm):
    user_task = StringField('todo', validators=[DataRequired()])
    save = SubmitField('save')
    done = BooleanField()
