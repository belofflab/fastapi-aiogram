import ormar
import sqlalchemy

from src.database.connection import database

metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
  database = database
  metadata = metadata


