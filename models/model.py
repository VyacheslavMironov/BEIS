from datetime import datetime
from configparser import ConfigParser
from email.policy import default
from enum import unique
from peewee import (
    SQL,
    MySQLDatabase, 
    Model, 
    CharField,
    BigIntegerField,
    DateField,
    ForeignKeyField
)


conf = ConfigParser()
conf.read(filenames='models/config.ini')

db = MySQLDatabase(
    conf['Mysql']['name'], 
    user=conf['Mysql']['user'], 
    password=conf['Mysql']['password'], 
    port=int(conf['Mysql']['port']), 
    host=conf['Mysql']['host']
)


class Users(Model):
    id = BigIntegerField(primary_key=True, unique=True,
                        constraints=[SQL('AUTO_INCREMENT')])
    name = CharField(max_length=30)
    surname = CharField(max_length=35)
    email = CharField(max_length=40, unique=True)
    token = CharField(max_length=500)
    password = CharField(max_length=500)
    created_at = DateField(default=datetime.now())

    class Meta:
        database = db # This model uses the "people.db" database.


class Messangers(Model):
    id = BigIntegerField(primary_key=True, unique=True,
                        constraints=[SQL('AUTO_INCREMENT')])
    title = CharField(max_length=25)

    class Meta:
        database = db # This model uses the "people.db" database.


class Messagers(Model):
    id = BigIntegerField(primary_key=True, unique=True,
                        constraints=[SQL('AUTO_INCREMENT')])
    user_ids = CharField(max_length=255)
    chat_name = CharField(max_length=120, default='')
    username = CharField(max_length=90, default='')
    name = CharField(max_length=90, default='')
    surname = CharField(max_length=90, default='')
    text = CharField(max_length=500, default='')
    img = CharField(max_length=180, default='')
    video = CharField(max_length=180, default='')
    voice = CharField(max_length=1000, default='')
    voice_text = CharField(max_length=1000, default='')
    file = CharField(max_length=180, default='')

    class Meta:
        database = db # This model uses the "people.db" database.


class Bots(Model):
    id = BigIntegerField(primary_key=True, unique=True,
                        constraints=[SQL('AUTO_INCREMENT')])
    user_id = ForeignKeyField(Users, backref='id')
    messenger_id = ForeignKeyField(Messangers, backref='id')
    # message_id = ForeignKeyField(Messangers, backref='id')
    name = CharField(max_length=30)
    recipient = CharField(max_length=50)
    token = CharField(max_length=255, unique=True)
    app_token = CharField(max_length=255, unique=True)
    hash_token = CharField(max_length=255, unique=True)
    created_at = DateField(default=datetime.now())

    class Meta:
        database = db # This model uses the "people.db" database.
