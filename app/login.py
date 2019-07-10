from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp


# is imported in routes.py
class RegistrationForm(FlaskForm):
    # first argument is an empty string, because placeholders are used
    username = StringField("", validators = [DataRequired(),Length(min = 2, max = 20), Regexp("^\w+$", message="Verwende nur Buchstaben, Ziffern und Unterstriche")], render_kw={"placeholder": "Username"})
    email = StringField("", validators = [DataRequired(), Email(message="Gültige Email-adresse erforderlich")], render_kw={"placeholder": "Email Adresse"})
    password = PasswordField("", validators = [DataRequired(), Length(min = 8, max = 20, message="Das Passwort muss zwischen 8 und 20 Zeichen haben")], render_kw={"placeholder": "Passwort"})
    confirm_password = PasswordField("", validators=[DataRequired(), EqualTo('password','Muss mit Passwort übereinstimmen')], render_kw={"placeholder": "Passwort wiederholen"})
    submit = SubmitField('Registrieren')

class LoginForm(FlaskForm):
    username = StringField("", validators= [DataRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField("", validators=[DataRequired()], render_kw={"placeholder": "Passwort"})
    remember = BooleanField('Angemeldet bleiben')
    submit = SubmitField('Login')