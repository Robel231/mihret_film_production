from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import Portfolio, BlogPost, ContactSubmission, Photo, Video, TextContent
from . import db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mihret.db'

    # Initialize Flask-Admin
    admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')

    # Add models to Flask-Admin
    admin.add_view(ModelView(Portfolio, db.session))
    admin.add_view(ModelView(BlogPost, db.session))
    admin.add_view(ModelView(ContactSubmission, db.session))
    admin.add_view(ModelView(Photo, db.session))
    admin.add_view(ModelView(Video, db.session))
    admin.add_view(ModelView(TextContent, db.session))

    # Initialize other extensions
    db.init_app(app)

    return app
from app.admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint, url_prefix='/admin')
