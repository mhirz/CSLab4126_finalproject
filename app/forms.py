from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp


# is imported in routes.py
class RegistrationForm(FlaskForm):
    # first argument is an empty string, because placeholders are used
    firstname = StringField("",
                            validators=[DataRequired(),
                                        Length(min=2, max =20),
                                        Regexp("^\w+$", message="Dein Name darf nur Buchstaben enthalten")],
                            render_kw={"placeholder": "Vorname"})

    lastname = StringField("",
                            validators=[DataRequired(),
                                        Length(min=2, max=20),
                                        Regexp("^\w+$", message="Dein Name darf nurt Buchstabebn enthalten")],
                            render_kw={"placeholder": "Nachname"})

    email = StringField("",
                        validators=[DataRequired(),
                                    Email(message="Gültige Email-adresse erforderlich")],
                        render_kw={"placeholder": "Email Adresse"})

    password = PasswordField("",
                             validators=[DataRequired(),
                                        Length(min=8, max=20, message="Das Passwort muss zwischen 8 und 20 Zeichen haben")],
                             render_kw={"placeholder": "Passwort"})

    confirm_password = PasswordField("",
                                     validators=[DataRequired(),
                                                 EqualTo('password','Muss mit Passwort übereinstimmen')],
                                     render_kw={"placeholder": "Passwort wiederholen"})

    submit = SubmitField('Registrieren')


class LoginForm(FlaskForm):
    email = StringField("",
                           validators=[DataRequired()],
                           render_kw={"placeholder": "Email Adresse"})

    password = PasswordField("",
                             validators=[DataRequired()],
                             render_kw={"placeholder": "Passwort"})

    remember = BooleanField('Angemeldet bleiben')
    submit = SubmitField('Login')


class ForgotPw(FlaskForm):
    firstname = StringField("",
                            validators=[DataRequired(),
                                        Length(min=2, max =20)],
                            render_kw={"placeholder": "Vorname"})
    lastname = StringField("",
                            validators=[DataRequired(),
                                        Length(min=2, max =20)],
                            render_kw={"placeholder": "Nachname"})
    email = StringField("",
                        validators=[DataRequired(),
                                    Email(message="Gültige Email-adresse erforderlich")],
                        render_kw={"placeholder": "Email Adresse"})
    submit = SubmitField('Email anfordern')


class AddBarter(FlaskForm):
    title = StringField("",
                        validators=[DataRequired(message="Du brauchst einen Titel"),
                                    Length(max=20, message="Titel darf maximal 20 Zeichen lang sein"),
                                    Regexp("^\w+$", message="Titel darf keine Sonderzeichen enthalten")],
                        render_kw={"placeholder": "Titel"})
    text = StringField("",
                       validators=[DataRequired(message="Bitte gib einen Beschreibungstext an"),
                                   Length(max=500, message="Titel darf maximal 5000 Zeichen lang sein")],
                       render_kw={"placeholder": "Beschreibungstext"})
    tag = StringField("",
                      validators=[],
                      render_kw={"placeholder": "Tags - durch Leerzeichen getrennt"})

    payments = StringField("",
                           validators=[],
                           render_kw={"placeholder": "Tauschangebote - durch Leerzeichen getrennt"})

class AddRequest(AddBarter):
    submit = SubmitField('Um Hilfe fragen')


class AddOffer(AddBarter):
    submit = SubmitField('Anbieten')