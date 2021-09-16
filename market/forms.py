from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from market.modules import Item, User
from wtforms.validators import EqualTo, Length, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label="Email address", validators=[Email() , DataRequired()])
    password1 = PasswordField(label='password',validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='password2', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')
