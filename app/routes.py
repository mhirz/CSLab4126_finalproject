from app import app, db, login_manager, models, bcrypt
from flask import render_template, flash, redirect, request
from flask_login import login_user, logout_user, login_required
from app.login import LoginForm, RegistrationForm
from app.models import User


# landingpage general
@app.route("/")
def index():
    return render_template('index.html')

from app import app, db, login_manager, models, bcrypt
from flask import render_template, flash, redirect, request
from flask_login import login_user, logout_user, login_required
from app.login import LoginForm, RegistrationForm
from app.models import User


# landingpage general
@app.route("/")
def index():
    return render_template('index.html')
