from flask import Blueprint, render_template, session
from app.models import Post
from app.db import get_db

# url_prefix prefixes every route with /dashboard; thus: /dashboard/edit/<id>
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
    db = get_db()
    posts = (
        db.query(Post)
        .filter(Post.user_id == session.get('user_id'))
        .order_by(Post.created_at.desc())
        .all()
    )

    return render_template(
        'dashboard.html',
        posts = posts,
        loggedIn = session.get('loggedIn')
    )

@bp.route('/edit/<id>')
def edit(id):
    return render_template('edit-post.html')