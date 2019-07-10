import os

class Config(object):
        SECRET_KEY = os.environ.get('secret_key') or 'thisisasecretkey'