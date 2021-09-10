from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from market.modules import Item


class RegisterForm(FlaskForm):
    username = StringField(label="Username")
    email_address = StringField(label="Email address")
    password1 = PasswordField(label='password')
    password2 = PasswordField(label='password2')
    submit = SubmitField(label='submit')
