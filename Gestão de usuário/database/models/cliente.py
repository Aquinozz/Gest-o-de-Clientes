from peewee import Model, CharField, DateTimeField
from database.database import db
import datetime

class Cliente(Model):
    nome = CharField()
    email = CharField(unique=True)
    data_criacao = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db 