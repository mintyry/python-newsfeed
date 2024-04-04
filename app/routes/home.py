# impoty functions
from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db

# Blueprint() lets us consolidste routes onto a single bp object that the parent app can register later.
# This is similar to Router in Express
bp = Blueprint('home', __name__, url_prefix='/')

# define two functions: index and login
# bp.route decorator turns the functions into routes.
# whatever fn returns becomes response; respond with templates
@bp.route('/')
def index():
  #get all posts
  # get_db() returns a session connection tied to this route's context
  db = get_db()
  # .all() returns all results as a list, save in variable "posts"
  posts = db.query(Post).order_by(Post.created_at.desc()).all()

  return render_template('homepage.html', posts=posts)

@bp.route('/login')
def login():
  return render_template('login.html')

# this route uses parameter (id)
# we can use the id parameter to query db for a single post
@bp.route('/post/<id>')
def single(id):
  #get single post by id
  db = get_db()
  # use filter method on connection obj to specify the SQL WHERE clause; use one() sted of all() to get single post.
  post = db.query(Post).filter(Post.id==id).one()

  return render_template('single-post.html', post=post)