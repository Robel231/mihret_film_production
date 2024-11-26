from datetime import datetime
from . import db

# Portfolio Model
class Portfolio(db.Model):
    __tablename__ = 'portfolio'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)  # URL of the image
    video_url = db.Column(db.String(200), nullable=True)   # URL of the video (optional)
    category = db.Column(db.String(50), nullable=False)    # E.g., "Film" or "Photo Shoot"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Portfolio {self.title}>'

# Blog Post Model
class BlogPost(db.Model):
    __tablename__ = 'blog_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)  # Optional cover image
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<BlogPost {self.title}>'

# Contact Form Submission Model
class ContactSubmission(db.Model):
    __tablename__ = 'contact_submission'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ContactSubmission {self.name}>'

# Photo Model (for storing photos in your admin)
class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Photo {self.title}>'

# Video Model (for storing videos in your admin)
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Video {self.title}>'

# Text Content Model (for storing text content like blog posts, descriptions)
class TextContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<TextContent {self.title}>'
