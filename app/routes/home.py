# impoty functions
from flask import Blueprint, render_template

# Blueprint() lets us consolidste routes onto a single bp object that the parent app can register later.
# This is similar to Router in Express
bp = Blueprint('home', __name__, url_prefix='/')

# define two functions: index and login
# bp.route decorator turns the functions into routes.
# whatever fn returns becomes response; respond with templates
@bp.route('/')
def index():
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')

# this route uses parameter (id)
@bp.route('/post/<id>')
def single(id):
  return render_template('single-post.html')