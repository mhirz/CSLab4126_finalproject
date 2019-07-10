from flask import Flask, Config

app = Flask(__name__)
app.config.from_object(Config)

#login_manager = LoginManager()
#login_manager.init_app(app)

from app import routes, models
