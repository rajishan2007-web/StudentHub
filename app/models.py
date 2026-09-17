# Import SQLAlchemy for database and UserMixin for login features
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()   # Create database object

class User(UserMixin, db.Model):   # User table (this will create a table in database)
    
    id = db.Column(db.Integer, primary_key=True)   # Unique ID for each user (Primary Key)
    
    username = db.Column(db.String(100), unique=True, nullable=False)   # Username (must be unique and cannot be empty)
    
    email = db.Column(db.String(150), unique=True, nullable=False)   # Email (must be unique and cannot be empty)
    
    password = db.Column(db.String(200), nullable=False)   # Password (stored as hashed string, not plain text)