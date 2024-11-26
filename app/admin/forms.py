from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired

class PhotoForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    file = FileField('Photo File', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Save')
class VideoForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    file = FileField('Video File', validators=[DataRequired()])
    submit = SubmitField('Save')