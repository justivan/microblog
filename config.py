import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') \
        or '7bebfb8333b87120a8fd42253b8aa4a2'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
        or 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
