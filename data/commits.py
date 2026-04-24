import sqlalchemy

from .db_session import SqlAlchemyBase

commits_to_branches = sqlalchemy.Table(
    "commits_to_branches",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("branches", sqlalchemy.Integer,
                      sqlalchemy.ForeignKey("branches.id")),
    sqlalchemy.Column("commits", sqlalchemy.Integer,
                      sqlalchemy.ForeignKey("commits.id"))
)


class Commits(SqlAlchemyBase):
    __tablename__ = "commits"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    sha1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    path = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    date_time = sqlalchemy.Column(sqlalchemy.String, nullable=True)
