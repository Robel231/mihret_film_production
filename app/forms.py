from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional
from flask_wtf.file import FileRequired, FileAllowed

# Contact Form
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Send Message')

# Portfolio Form
class PortfolioForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    
    # Image and video file upload validation
    image = FileField('Image', validators=[
        FileRequired(), 
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])  # Ensure the image is a JPG, PNG, or JPEG
    
    video = FileField('Video', validators=[
        Optional(),  # Video is optional
        FileAllowed(['mp4', 'mov', 'avi'], 'Videos only!')
    ])  # Ensure the video is of valid format (mp4, mov, avi)
    
    # Category selection with validation
    category = SelectField(
        'Category',
        choices=[('film', 'Film'), ('photo', 'Photo Shoot')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Add to Portfolio')

# Blog Post Form
class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    
    # Optional file upload for blog cover image
    image = FileField('Cover Image', validators=[
        Optional(),  # Optional field
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])  # Ensure the cover image is an image file
    
    submit = SubmitField('Publish Blog Post')
