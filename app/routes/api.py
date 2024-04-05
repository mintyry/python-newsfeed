from flask import Blueprint, request, jsonify
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()

# creates new user
    newUser = User(
        username = data['username'],
        email = data['email'],
        password = data['password']
    )

    # save in database
    # preps the INSERT statement
    db.add(newUser)
    # updates database
    db.commit()

    return jsonify(id = newUser.id)