# Import Blueprint and render_template
from flask import Blueprint, render_template

# Create blueprint for main routes
main = Blueprint('main', __name__)

# Home route
@main.route('/')
def home():
    # This will load your homepage UI
    return render_template('index.html')