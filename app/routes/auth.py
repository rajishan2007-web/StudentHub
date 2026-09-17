# Import required modules
from flask import Blueprint, render_template, request, redirect, url_for

# For password hashing (security)
from werkzeug.security import generate_password_hash, check_password_hash

# Import database and User model
from ..models import db, User

# Import login functions
from flask_login import login_user, logout_user, login_required

# Create blueprint (group of routes)
auth = Blueprint('auth', __name__)


# ---------------- SIGNUP ----------------
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    
    # If user submits form
    if request.method == 'POST':
        
        # Get data from form
        username = request.form.get('username')
        email = request.form.get('email')
        
        # Convert password into secure hash
        password = generate_password_hash(request.form.get('password'))

        # Create new user object
        new_user = User(username=username, email=email, password=password)
        
        # Save user to database
        db.session.add(new_user)
        db.session.commit()

        # After signup, redirect to login page
        return redirect(url_for('auth.login'))

    # If GET request → just show signup page
    return render_template('auth/signup.html')


# ---------------- LOGIN ----------------
@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        
        # Get email and password from form
        email = request.form.get('email')
        password = request.form.get('password')

        # Find user in database
        user = User.query.filter_by(email=email).first()

        # Check if user exists and password is correct
        if user and check_password_hash(user.password, password):
            
            # Log the user in
            login_user(user)
            
            # Redirect to home page
            return redirect('/')

    # Show login page
    return render_template('auth/login.html')


# ---------------- LOGOUT ----------------
@auth.route('/logout')
@login_required  # Only logged-in users can logout
def logout():
    
    # Logout user
    logout_user()
    
    # Redirect to home page
    return redirect('/')