from flask import Blueprint, render_template

# url_prefix prefixes every route with /dashboard; thus: /dashboard/edit/<id>
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
    return render_template('dashboard.html')

@bp.route('/edit/<id>')
def edit(id):
    return render_template('edit-post.html')