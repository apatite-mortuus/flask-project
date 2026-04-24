from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class BranchForm(FlaskForm):
    parent = SelectField("Исток", validators=[DataRequired()])
    title = StringField("Название", validators=[DataRequired()])
    submit = SubmitField("Создать")
