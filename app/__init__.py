# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
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

# Initialize extensions
db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    
    # Configuration settings
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mihret.db'  # Use SQLite during development
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions with app
    db.init_app(app)
    csrf.init_app(app)
    
    # Import and register blueprints (routes)
    from .routes import main
    app.register_blueprint(main)
    
    # Create database tables (if not already created)
    with app.app_context():
        db.create_all()
    
    return app
