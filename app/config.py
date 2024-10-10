from peewee import SqliteDatabase

local_database = SqliteDatabase('database.db')


def startup_db():
    local_database.connect()

    from app.models import CategoriaDataBase, TurmaDataBase, FuncionarioDataBase

    local_database.create_tables([CategoriaDataBase, TurmaDataBase, FuncionarioDataBase])


def shutdown_db():
    local_database.close()