# ================================
# config.py - CONFIGURATION FILE
# This file stores all the settings
# that our website needs to run
# ================================

import os  # os helps us read system environment variables

class Config:
    
    SECRET_KEY = os.environ.get("SECRET_KEY") or "mysecretkey123" 
    # SECRET_KEY is used to protect forms and login sessions
    # It's like a password for your website's security system

    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    # This tells Flask where our database file is located
    # It will be created automatically inside the instance/ folder

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # This turns off a feature we don't need
    # Keeps things clean and avoids unnecessary warnings