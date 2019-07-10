from app import app
from flask import render_template, request, flash
from app.login import LoginForm, RegistrationForm

# landingpage
@app.route("/index")
@app.route("/home")
@app.route("/")
def index():
    return render_template('index.html', title="Startseite")

# login
@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm
    return render_template('login.html', title="Login", form=form)

# register
@app.route("/register")
def register():
    return render_template('register.html', title="Registrieren")

@app.route("/about")
def about():

    # team members could be loaded from database not hard coded
    team = [["Dave", "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"],
            ["Markus", "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"],]

    return render_template('about.html', title='About', team=team)


