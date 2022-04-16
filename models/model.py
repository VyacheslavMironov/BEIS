from datetime import datetime
from configparser import ConfigParser
from email.policy import default
from peewee import (
    SQL,
    MySQLDatabase, 
    Model, 
    CharField,
    BigIntegerField,
    DateField
)


conf = ConfigParser()
conf.read(filenames='config.ini')

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
    name = CharField()
    surname = CharField()
    token = CharField()
    created_at = DateField(default=datetime.now())

    class Meta:
        database = db # This model uses the "people.db" database.


