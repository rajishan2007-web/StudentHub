from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import db, Post

blog = Blueprint("blog", __name__, url_prefix="/blog")


@blog.route('/')
def list_posts():
    query = request.args.get('q', '').strip()

    if query:
        posts = Post.query.filter(
            (Post.title.ilike(f'%{query}%')) | (Post.content.ilike(f'%{query}%'))
        ).order_by(Post.created_at.desc()).all()
    else:
        posts = Post.query.order_by(Post.created_at.desc()).all()

    return render_template('blog/list.html', posts=posts, query=query)


@blog.route('/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        post = Post(title=title, content=content, author=current_user)
        db.session.add(post)
        db.session.commit()

        flash('Post published successfully!', 'success')
        return redirect(url_for('blog.list_posts'))

    return render_template('blog/new.html')


@blog.route('/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog/view.html', post=post)


@blog.route('/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.user_id != current_user.id:
        flash('You can only delete your own posts.', 'error')
        return redirect(url_for('blog.list_posts'))

    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully.', 'success')
    return redirect(url_for('blog.list_posts'))
