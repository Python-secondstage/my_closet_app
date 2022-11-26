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
    name = CharField()  # 文字

    class Meta:
        database = db
        table_name = "clothe"


db.create_tables([Clothe])
