from playhouse.db_url import connect
from peewee import Model
from peewee import CharField
from peewee import IntegerField
from flask_login import UserMixin


db = connect("sqlite:///peewee_db.sqlite")

if not db.connect():
    print("接続NG")
    exit()
print("接続OK")


class Clothe(UserMixin, Model):
    id = IntegerField(primary_key=True)  # 数字
    # name = CharField()  # 文字
    file = CharField()  # 画像
    type = CharField()  # 種類

    class Meta:
        database = db
        table_name = "clothe"


db.create_tables([Clothe])


class Type(UserMixin, Model):
    id = IntegerField(primary_key=True)  # 数字
    type1 = CharField()  # 種類1
    type2 = CharField()  # 種類2

    class Meta:
        database = db
        table_name = "type"


db.create_tables([Type])


class User(UserMixin, Model):
    id = IntegerField(primary_key=True)  # 数字
    name = CharField()  # 文字
    password = CharField()  # 文字

    class Meta:
        database = db
        table_name = "user"


db.create_tables([User])
