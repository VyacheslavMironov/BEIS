from datetime import datetime
from configparser import ConfigParser
from email.policy import default
from peewwee import (
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


<<<<<<< HEAD
class Users(Model):
    id = BigIntegerField(primary_key=True, unique=True,
                        constraints=[SQL('AUTO_INCREMENT')])
    name = CharField()
    surname = CharField()
    token = CharField()
    created_at = DateField(default=datetime.now())

    class Meta:
        database = db # This model uses the "people.db" database.
=======
print( DB().connect() )
#как же я заебался с этим удалённым аккаунтом гита#
#который раз#
>>>>>>> 9f8fa3045634ac21ca7796d3b37f6a7d25ebb974
