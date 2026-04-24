import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Audiofile(SqlAlchemyBase):
    __tablename__ = "audiofiles"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    path_to_file = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    posted = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), nullable=True)
    date_time = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = orm.relationship("User")
    likes = orm.relationship("Likes", back_populates="file")
    dislikes = orm.relationship("Dislikes", back_populates="file")
