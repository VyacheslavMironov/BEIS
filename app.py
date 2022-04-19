# !/usr/bin/python 
# -*- coding: utf-8 -*-
import bcrypt
from cryptocode import encrypt, decrypt
from datetime import datetime, timedelta, timezone
from random import choice
from string import ascii_lowercase
from logging import basicConfig, DEBUG, error
from peewee import IntegrityError
from configparser import ConfigParser
# from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
    JWTManager,
    set_access_cookies,
    unset_jwt_cookies
)
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


# basicConfig(filename='log/error.log')
# ------------------------------------------------
# Создание таблиц перед запуском приложения
# ------------------------------------------------
db.connect()
db.create_tables([Users, Messangers, Messagers, Bots])
db.close()
# ------------------------------------------------
app = Flask(__name__)
# ------------------------------------------------
# JWT генератор
# ------------------------------------------------

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)
# If true this will only allow the cookies that contain your JWTs to be sent
# over https. In production, this should always be set to True
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this in your code!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
# ------------------------------------------------
# Добавление заголовков передачи данных с других хостов
# ------------------------------------------------

cors = CORS(app, resources={r"/*": {"origins": "*"}}, headers='Content-Type')
app.config['CORS_HEADERS'] = 'Content-Type'


@app.after_request
def refresh_expiring_jwts(response):
    """
    Используя обратный вызов `after_request`, мы обновляем любой токен, 
    который находится в пределах 30 минут истекает. Измените временные 
    дельты в соответствии с потребностями вашего приложения.
    """
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response


@app.route('/api/v1/signup', methods=['POST'])
@cross_origin()
def registration():
    if request.method == "POST":
        name = request.get_json().get("data")["name"]
        surname = request.get_json().get("data")["surname"]
        email = request.get_json().get("data")["email"]
        token = ''.join(choice(ascii_lowercase) for i in range(30))
        password = request.get_json().get("data")["password"]
        created_at = datetime.now()

        # Проверка на заполненость данных
        if name is None or surname is None or email is None or password is None:
            # return abort(400)
            return (jsonify({'response': False, 'message': 'Введите все данные'}), 200)
        else:
            try:
                # Добавление пользователя
                user = Users.insert(name = name, surname = surname, email = email, 
                    token = token, password = password, created_at = created_at ).execute()

                if user:
                    # Сохранение
                    # return (jsonify({'response': True, 'message': 'Данные сохранены!'}), 200)
                    access_token = create_access_token(identity={"email": email})
                    return {
                        'access_token': access_token, 
                        'response': True, 
                        'message': 'Данные сохранены!'}, 200

            except IntegrityError as e:
                # error(msg=e)
                return (jsonify({'response': False, 'message': 'Почта уже занята!'}), 200)


@app.route('/api/v1/signin', methods=['POST'])
def login():
    if request.method == 'POST':
        # email = request.form.get("email")
        # password = request.form.get("password")
        email = request.get_json().get("data")["email"]
        password = request.get_json().get("data")["password"]

        if email is None or password is None:
            return jsonify({'response': False, 'message': 'Введите данные!'}), 401
        
        user = Users.get(Users.email == email.strip())
        if not user:
            return jsonify({'response': False, 'message': 'Страница не найдена!'}), 404

        if password == user.password:
            access_token = create_access_token(identity={
                                                            'name': user.name,
                                                            'surname': user.surname,
                                                            'email': user.email,
                                                            'token': user.token
                                                        })
            set_access_cookies(jsonify({"message": "Успех!"}), access_token)
            return jsonify({
                "access_token": access_token, 
                'message': 'Добро пожаловать!'
            }), 200
        else:
            return jsonify({'message': 'Ошибка, попробуйте ещё раз!'}), 400

@app.route('/api/v1/', methods=['GET'])
@jwt_required()
def index():
    pass


@app.route('/api/v1/signout', methods=['GET'])
@jwt_required()
def signout():
    response = jsonify({'response': True, 'message': 'Пока ёпта!'})
    unset_jwt_cookies(response)
    return response


@app.route('/profile', methods=['GET','POST'])
@jwt_required()
def profile():
    return jsonify({'response': True, 'message': 'Привет ёпта!'})


@app.route('/api/v1/bots', methods=['GET'])
def bot_all():
    pass

@app.route('/api/v1/bot-create', methods=['GET', 'POST'])
def bot_create():
    pass

@app.route('/api/v1/bots-info', methods=['GET'])
def bot_info():
    pass

@app.route('/api/v1/bots-drop', methods=['GET', 'DELETE'])
def bot_drop():
    pass

@app.route('/api/v1/bots-update', methods=['GET', 'PUT'])
def bot_update():
#     pass


if __name__ == "__main__":
    app.run(debug=True)
