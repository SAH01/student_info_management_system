import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess!')
    SQLALCHEMY_DATABASE_URI = r'sqlite:///C:/Users/bitte/student_info.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
