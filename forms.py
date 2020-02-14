from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class LoginForm(FlaskForm):
    name = StringField('Twój nick', validators=[Required()])
    room = StringField('Pokój', validators=[Required()])
    submit = SubmitField('Wejdź do czatu')