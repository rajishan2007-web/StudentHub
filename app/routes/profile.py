from flask import Blueprint, render_template
from flask_login import login_required, current_user

profile = Blueprint("profile", __name__, url_prefix="/profile")


@profile.route('/')
@login_required
def view_profile():
    posts = sorted(current_user.posts, key=lambda p: p.created_at, reverse=True)
    return render_template('profile/view.html', posts=posts)
