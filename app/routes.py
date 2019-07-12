#from app import app
from flask import Flask, render_template, request, flash, session, url_for, abort, redirect
from app.forms import LoginForm, RegistrationForm, AddOffer, AddRequest, ForgotPw
from app.models import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', title="Startseite")


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if request.method == 'Post':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']

        try:
            password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        except ValueError:
            flash('Ein Passwort ist erforderlich', 'warning')
            return redirect('/register')

        if form.validate_on_submit():
            # username must not exist in the database yet
            if not User(email).set_password(password).register():
                flash('Diese Email wird bereits verwendet. Bitte wähle eine andere', 'warning')
                return redirect('/register')

            # if registration successful -> redirected to login
            flash(f'{form.firstname.data} es wurde ein Account für dich erstellt!', 'success')
            return redirect('/login')

    return render_template('register.html', title = 'Register', form = form)


@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        # retrieve input values from the input fields
        email = request.form['email']
        password = request.form['password']

        user = User(email)

        # if form validates correctly
        if form.validate_on_submit():
            if not user.verify_password(password):
                flash("Please try again!", 'warning')
                return redirect('/login')
            else:
                session['username'] = user.username
                flash(f'{form.firstname.data} du bist erfolgreich angemeldet!', 'success')
                return redirect('/')
    return render_template('login.html', title='Login', form=form)


@app.route('/forgot_pw', methods=['GET','POST'])
def forgot_pw():
    form = ForgotPw()
    return render_template('forgot_pw.html', title='Passwort zurücksetzen', form=form)


@app.route('/add_request', methods=['GET', 'POST'])
def add_request():
    form = AddRequest()
    user = User(session['email'])
    title = request.form['title']
    tags = request.form['tags']
    text = request.form['text']
    payment = request.form['payment']

    if form.validate_on_submit():
        user.add_request(title, tags, text, payment)
        return redirect(url_for('/index'))

    return render_template('forgot_pw.html', title='Login', form=form)


@app.route('/add_offer', methods=['GET', 'POST'])
def add_offer():
    form = AddOffer()
    user = User(session['email'])
    title = request.form['title']
    tags = request.form['tags']
    text = request.form['text']
    payment = request.form['payment']

    user.add_offer(title, tags, text, payment)
    return redirect(url_for('/index'))


@app.route("/about")
def about():

    # team members could be loaded from database not hard coded
    team = [["Dave", "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"],
            ["Hirzi", "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"],]

    return render_template('about.html', title='About', team=team)


