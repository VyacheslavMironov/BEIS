# !/usr/bin/python 
# -*- coding: utf-8 -*-
from cryptocode import encrypt, decrypt
from datetime import datetime
from random import choice
from string import ascii_lowercase
from logging import basicConfig, DEBUG, error, info
from peewee import IntegrityError
from configparser import ConfigParser
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin
from flask import (
    Flask,
    make_response,
    render_template, 
    request, 
    jsonify, 
    abort,
    url_for
)

from models.model import db, Users, Messangers, Messagers, Bots


basicConfig(filename='log/error.log', level=DEBUG, filemode='w',)
# ------------------------------------------------
# Создание таблиц перед запуском приложения
# ------------------------------------------------
db.connect()
db.create_tables([Users, Messangers, Messagers, Bots])
db.close()
# ------------------------------------------------
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, headers='Content-Type')
app.config['CORS_HEADERS'] = 'Content-Type'


# @app.route('/', methods=['GET'])
# def index():
#     pass

@app.route('/api/v1/signup', methods=['GET', 'POST'])
@cross_origin()
def registration():
    if request.method == "POST":
        name = request.get_json().get("data")["name"]
        surname = request.get_json().get("data")["surname"]
        email = request.get_json().get("data")["email"]
        token = ''.join(choice(ascii_lowercase) for i in range(30))
        password = encrypt(request.get_json().get("data")["password"], 'wow')
        created_at = datetime.now()

        # Проверка на заполненость данных
        if name is None or surname is None or email is None or password is None:
            return abort(400)
        else:
            try:
                # Добавление пользователя
                user = Users.insert(name = name, surname = surname, email = email, 
                    token = token, password = password, created_at = created_at ).execute()

                if user:
                    # Сохранение
                    return (jsonify({'response': True, 'token': token}), 200)
                else:
                    return (jsonify({'response': False, 'token': None}), 200)
            except IntegrityError as e:
                error(msg=e)


# @app.route('/sigin', methods=['GET', 'POST'])
# def login():
#     pass

# @app.route('/profile', methods=['GET','POST'])
# def profile():
#     pass

# @app.route('/bots', methods=['GET'])
# def bot_all():
#     pass

# @app.route('/bot-create', methods=['GET', 'POST'])
# def bot_create():
#     pass

# @app.route('/bots-info', methods=['GET'])
# def bot_info():
#     pass

# @app.route('/bots-drop', methods=['GET', 'DELETE'])
# def bot_drop():
#     pass

# @app.route('/bots-update', methods=['GET', 'PUT'])
# def bot_update():
#     pass


if __name__ == "__main__":
    app.run(debug=True)
