# !/usr/bin/python 
# -*- coding: utf-8 -*-
from configparser import ConfigParser
from flask_httpauth import HTTPBasicAuth
from flask import (
    Flask,
    make_response,
    render_template, 
    request, 
    jsonify, 
    abort,
    url_for
)

from models.model import db, Users



# ------------------------------------------------
# Создание таблиц перед запуском приложения
# ------------------------------------------------
# db.connect()
# db.create_tables([Users])
# db.close()
# ------------------------------------------------
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    pass

@app.route('/signup', methods=['GET', 'POST'])
def registration():
    pass

@app.route('/sigin', methods=['GET', 'POST'])
def login():
    pass

@app.route('/profile', methods=['GET','POST'])
def profile():
    pass

@app.route('/bots', methods=['GET'])
def bot_all():
    pass

@app.route('/bot-create', methods=['GET', 'POST'])
def bot_create():
    pass

@app.route('/bots-info', methods=['GET'])
def bot_info():
    pass

@app.route('/bots-drop', methods=['GET', 'DELETE'])
def bot_drop():
    pass

@app.route('/bots-update', methods=['GET', 'PUT'])
def bot_update():
    pass


if __name__ == "__main__":
    app.run()
