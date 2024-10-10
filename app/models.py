from peewee import (
    AutoField,
    CharField,
    ForeignKeyField,
    Model,
    IntegerField,
    DateField,
)

from app.config import local_database

class FuncionarioDataBase(Model):
    id = AutoField()
    nome = CharField()
    email = CharField()
    cargo = CharField()

    class Meta:
        database = local_database

class CategoriaDataBase(Model):
    id = AutoField()
    nome = CharField()

    class Meta:
        database = local_database

class TurmaDataBase(Model):
    id = AutoField()
    nome = CharField()
    categoria = ForeignKeyField(model=CategoriaDataBase, backref='categorias')

    class Meta:
        database = local_database