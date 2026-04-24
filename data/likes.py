import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Likes(SqlAlchemyBase):
    __tablename__ = "likes"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    audiofile = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("audiofiles.id"), nullable=True)
    author_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), nullable=True)
    user = orm.relationship("User")
    file = orm.relationship("Audiofile")
