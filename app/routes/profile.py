from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from ..models import db, User

profile = Blueprint("profile", __name__, url_prefix="/profile")


@profile.route('/')
@login_required
def view_profile():
    posts = sorted(current_user.posts, key=lambda p: p.created_at, reverse=True)
    return render_template('profile/view.html', posts=posts)


@profile.route('/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        new_username = request.form.get('username').strip()
        new_email = request.form.get('email').strip()
        new_password = request.form.get('password', '').strip()

        existing_user = User.query.filter(User.username == new_username, User.id != current_user.id).first()
        if existing_user:
            flash('Username already taken.', 'error')
            return redirect(url_for('profile.edit_profile'))

        existing_email = User.query.filter(User.email == new_email, User.id != current_user.id).first()
        if existing_email:
            flash('Email already in use.', 'error')
            return redirect(url_for('profile.edit_profile'))

        current_user.username = new_username
        current_user.email = new_email

        if new_password:
            if len(new_password) < 6:
                flash('Password must be at least 6 characters.', 'error')
                return redirect(url_for('profile.edit_profile'))
            current_user.password = generate_password_hash(new_password)

        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile.view_profile'))

    return render_template('profile/edit.html')
