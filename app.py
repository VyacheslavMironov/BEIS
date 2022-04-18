# !/usr/bin/python 
# -*- coding: utf-8 -*-
from hashlib import sha1
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

from models.model import db, Users, Messangers, Messagers, Bots



# ------------------------------------------------
# Создание таблиц перед запуском приложения
# ------------------------------------------------
db.connect()
db.create_tables([Users, Messangers, Messagers, Bots])
db.close()
# ------------------------------------------------
app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     pass

@app.route('/signup', methods=['POST'])
def registration():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        token = request.form.get("token")
        password = request.form.get("password")
        created_at = request.form.get("created_at")

        # Проверка на заполненость данных
        if name is None or surname is None or password is None:
            return abort(400)
        

        return (jsonify(
            {
                'name': name, 
                'surname': surname, 
                'token': token, 
                'password': password,
                'created_at': created_at
            }
        ), 200)

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
