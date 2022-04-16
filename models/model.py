from sqlite3 import Cursor
from peewee import  MySQLDatabase


class DB:
    def __init__(self) -> None:
        self.name = "beis"
        self.user = "root"
        self.password = "263685"
        self.port = 3306
        self.host = "localhost"
        

    def connect(self) -> list:
        connect=MySQLDatabase(self.name, user=self.user, password=self.password, port=self.port, host=self.host)
        cursor=connect.cursor()
        return [connect, cursor]


print( DB().connect() )
#как же я заебался с этим удалённым аккаунтом гита#
