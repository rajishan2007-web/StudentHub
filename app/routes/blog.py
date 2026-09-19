from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import db, Post

blog = Blueprint("blog", __name__, url_prefix="/blog")


@blog.route('/')
def list_posts():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('blog/list.html', posts=posts)


@blog.route('/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        post = Post(title=title, content=content, author=current_user)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('blog.list_posts'))

    return render_template('blog/new.html')


@blog.route('/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog/view.html', post=post)
