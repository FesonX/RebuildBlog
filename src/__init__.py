# -*- coding:utf-8 _*-  
""" 
@file: __init__.py.py 
@time: 2020-05-24 16:06
@author:FesonX 
@contact: fesonx@foxmail.com
@site: github.com/FesonX 
@software: PyCharm 
"""
from os import urandom, path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import BASE_DIR


def create_app() -> Flask:
    flask_app = Flask(__name__, template_folder=BASE_DIR + '/src/templates',
                      static_folder=BASE_DIR + '/src/static')
    flask_app.config.from_pyfile(BASE_DIR + '/config.py')
    instance_folder = flask_app.instance_path or BASE_DIR + '/instance'
    if path.isdir(instance_folder):
        # u should manually create instance config,
        # and add SQLALCHEMY_DATABASE_URI to connect the database.
        flask_app.config.from_pyfile(instance_folder + '/config.py')

    if not flask_app.config.get('SQLALCHEMY_DATABASE_URI'):
        raise ValueError('Fail to find `SQLALCHEMY_DATABASE_URI`, did u config yet?')
    random_bytes = urandom(64) if flask_app.config.get('mode') == 'pro' else b'UnderDeveloping'
    flask_app.secret_key = random_bytes
    return flask_app


app = create_app()
db = SQLAlchemy(app)
