#from app import app
from flask import Flask, render_template, request, flash, session, url_for, abort, redirect
from app.forms import LoginForm, RegistrationForm, AddOffer, AddRequest, ForgotPw
from app.models import *

app = Flask(__name__)

@app.route("/")
def index():
    # TODO: function to get requests & offers from DB
    offers = [{"title":"Englisch Nachhilfe",
             "text":"Falls wer Hilfe in Englisch in der Oberstufe braucht, stehe ich gern zur Verfügung",
             "tag":"#nachhilfe #englisch #schule"},{"title":"Englisch Nachhilfe",
             "text":"Falls wer Hilfe in Englisch in der Oberstufe braucht, stehe ich gern zur Verfügung",
             "tag":"#nachhilfe #englisch #schule"},{"title":"Englisch Nachhilfe",
             "text":"Falls wer Hilfe in Englisch in der Oberstufe braucht, stehe ich gern zur Verfügung",
             "tag":"#nachhilfe #englisch #schule"},{"title":"Englisch Nachhilfe",
             "text":"Falls wer Hilfe in Englisch in der Oberstufe braucht, stehe ich gern zur Verfügung",
             "tag":"#nachhilfe #englisch #schule"}]
    requests = [{"title": "Anhänger",
             "text": "Es wär super wenn mir wer einen Anhänger borgen könnte, damit ich mein Motorrad in die Werkstatt bringen kann",
             "tag": "#anhänger #transpoert #auto"},{"title": "Anhänger",
             "text": "Es wär super wenn mir wer einen Anhänger borgen könnte, damit ich mein Motorrad in die Werkstatt bringen kann",
             "tag": "#anhänger #transpoert #auto"},{"title": "Anhänger",
             "text": "Es wär super wenn mir wer einen Anhänger borgen könnte, damit ich mein Motorrad in die Werkstatt bringen kann",
             "tag": "#anhänger #transpoert #auto"},{"title": "Anhänger",
             "text": "Es wär super wenn mir wer einen Anhänger borgen könnte, damit ich mein Motorrad in die Werkstatt bringen kann",
             "tag": "#anhänger #transpoert #auto"},{"title": "Anhänger",
             "text": "Es wär super wenn mir wer einen Anhänger borgen könnte, damit ich mein Motorrad in die Werkstatt bringen kann",
             "tag": "#anhänger #transpoert #auto"}]
    return render_template('index.html', title="Startseite", offers=offers, requests=requests)


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = bcrypt.encrypt(request.form['password'])
        # query iuser from database
        #user =

        if form.validate_on_submit():
            # username must not exist in the database yet
            if not User(firstname, lastname, email, password).register():
                flash('Diese Email wird bereits verwendet. Bitte wähle eine andere', 'warning')
                return redirect('/register')

            # if registration successful -> redirected to login
            flash(f'{form.firstname.data} es wurde ein Account für dich erstellt!', 'success')
            return redirect('/login')
        flash('Well!', 'warning')

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
    if request.method == 'GET':
        try:
            User(session['email'])
            #TODO implement form to add new request
        except:
            flash('Melde dich bitte zuerst an:', 'warning')
            return redirect('/login')
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
    if not User(session['email']):
        flash('Melde dich bitte zuerst an:', 'warning')
        return redirect('/login')
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


