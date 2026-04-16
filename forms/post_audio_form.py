from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms import StringField, DateTimeField, SubmitField
from wtforms.validators import DataRequired


class PostAudioForm(FlaskForm):
    file = FileField("Аудиофайл", validators=[FileRequired(), FileAllowed(["mp3", "ogg", "flac", "wav", "m4a"])])
    title = StringField("Название", validators=[DataRequired()])
    author = StringField("Автор", validators=[DataRequired()])
    submit = SubmitField("Отправить")
