#from app import app
from flask import Flask, render_template, request, flash, session, url_for, abort, redirect
from app.forms import LoginForm, RegistrationForm, AddBarter, AddOffer, AddRequest, ForgotPw
from app.models import *
import bcrypt

app = Flask(__name__)

@app.route("/")
def index():
    # TODO: function to get requests & offers from DB
    
    requests = Request.get_all_requests()
    offers = Request.get_all_offers()

    # offers = [{"title":"Englisch Nachhilfe",
    #          "text":"Falls wer Hilfe in Englisch in der Oberstufe braucht, stehe ich gern zur Verfügung",
    #          "tag":"#nachhilfe #englisch #schule"}]

    # requests = [{"title": all_requests["r"]["name"]
    #          "text": "Es wär super wenn mir wer einen Anhänger borgen könnte, damit ich mein Motorrad in die Werkstatt bringen kann",
    #          "tag": "#anhänger #transpoert #auto"}]

    return render_template('index.html', title="Startseite", offers=offers, requests=requests)


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        # password = bcrypt.encrypt(request.form['password']) -- old
        password = bcrypt.hashpw(str(request.form['password']).encode('utf-8'), bcrypt.gensalt())
        # query iuser from database
        user = User(firstname, 
                lastname,
                email,
                password)
        
        if form.validate_on_submit():
            # username must not exist in the database yet
            # if not User(firstname, lastname, email, password).register():
            if(user.register() == False):
                flash('Diese Email wird bereits verwendet. Bitte wähle eine andere', 'warning')
                return redirect('/register')

            if(user.register() == True):#registration successful -> redirected to login
                # flash(f'{form.firstname.data} es wurde ein Account für dich erstellt!', 'success')
                flash('Es wurde ein Account für dich erstellt!', 'success')
                return redirect('/login')

        # flash('Well!', 'warning')

    return render_template('register.html', title = 'Register', form = form)


@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        # retrieve input values from the input fields
        email = request.form['email']
        password = request.form['password']

        user = User.find_by_email(email)
        

        # if form validates correctly
        if form.validate_on_submit():
            if not user.verify_password(password):
                flash("Please try again!", 'warning')
                return redirect('/login')
            else:
                session['email'] = user.email
                flash(f'{user.firstname} du bist erfolgreich angemeldet!', 'success')
                return redirect('/')
    return render_template('login.html', title='Login', form=form)


@app.route('/forgot_pw', methods=['GET','POST'])
def forgot_pw():
    form = ForgotPw()
    return render_template('forgot_pw.html', title='Passwort zurücksetzen', form=form)


@app.route('/add_request', methods=['GET', 'POST'])
def add_request():
    form = AddBarter()

    if request.method == 'POST':
        # user = User(session['email'])
        user = User.find_by_email(session['email'])
        title = request.form['title']
        # tags = request.form['tags'] #deactivated for testing
        text = request.form['text']
        # payment = request.form['payment'] #deactivated for testing
        if form.validate_on_submit():
            # user.add_request(title, tags, text, payment)
            user.add_request(title, text)
            return redirect(url_for('index'))

    else:
        try:
            # for testing -> logged in user is simulated
            # uncommend following line
            User.find_by_email(session['email'])
            # user = True
        except:
            flash('Melde dich bitte zuerst an:', 'warning')
            return redirect('/login')
    return render_template('add_request.html', title='Suche Hilfe', form=form)


@app.route('/add_offer', methods=['GET', 'POST'])
def add_offer():
    form = AddBarter()

    if request.method == 'POST':
        # user = User(session['email'])
        user = User.find_by_email(session['email'])
        title = request.form['title']
        # tags = request.form['tags'] #deactivated for testing
        text = request.form['text']
        # payment = request.form['payment'] #deactivated for testing
        if form.validate_on_submit():
            # user.add_offer(title, tags, text, payment)
            user.add_offer(title, text)
            return redirect(url_for('index'))

    else:
        try:
            # for testing -> logged in user is simulated
            # uncommend following line
            User.find_by_email(session['email'])
            # user = True
        except:
            flash('Melde dich bitte zuerst an:', 'warning')
            return redirect('/login')
    return render_template('add_offer.html', title='Suche Hilfe', form=form)

@app.route("/about")
def about():

    # team members could be loaded from database not hard coded
    team = [["Dave", "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"],
            ["Hirzi", "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"],]

    return render_template('about.html', title='About', team=team)


