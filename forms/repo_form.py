from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RepoForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
    description = StringField("Описание")
    submit = SubmitField("Создать")
