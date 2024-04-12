from flask import Blueprint, request, jsonify, session
from app.models import User, Post, Comment, Vote
from app.db import get_db
import sys

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()

    try:

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
    except:
        print(sys.exc_info()[0])
        # insert failed, so rollback the commit and send error to front end
        db.rollback()
        return jsonify(message = 'Signup failed'), 500
    
    session.clear()
    session['user_id'] = newUser.id
    session['loggedIn'] = True
    return jsonify(id = newUser.id)

@bp.route('/users/logout', methods=['POST'])
def logout():
   #remove session variables
   session.clear()
   return '', 204

@bp.route('/users/login', methods=['POST'])
def login():
        data = request.get_json()
        db = get_db()

# query User table, filter to look through each user's email and find where the data's email is equaivalent to the user that has that email
# essentually checking is uer exists; if they do, must verify password.
        try:
             user = db.query(User).filter(User.email == data['email']).one()
        except:
             print(sys.exc_info()[0])
             return jsonify(mesage =  'Incorrect credentials'), 400
        
        # data['passowrd'] is the second parameter for verify_password() because self is first.
        if user.verify_password(data['password']) == False:
            #  if email or password is wrong/doesnt match, 400 error; if correct, session is created
             return jsonify(message = 'Incorrect credentials'), 400
        
        session.clear()
        session['user_id'] = user.id
        session['loggedIn'] = True
        return jsonify(id = user.id)

@bp.route('/comments', methods=['POST'])
def comment():
    #  connects to db
    # capture posted data with get_json()
    # create new comment using the returned dictionary
    data = request.get_json()
    db = get_db()
    
    try:
        #   create new comment
        newComment = Comment(
             comment_text = data['comment_text'],
             post_id = data['post_id'],
             user_id = session.get('user_id')
        )

        db.add(newComment)
        db.commit()
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message = 'Comment failed'), 500
    
    return jsonify(id = newComment.id)

@bp.route('/posts/upvote', methods=['PUT'])
def upvote():
     data = request.get_json()
     db = get_db()

     try:
          # create a new vote with incoming id and session id
          newVote = Vote(
               post_id = data['post_id'],
               user_id = session.get('user_id')
            )

          db.add(newVote)
          db.commit()
     except:
        print(sys.exc_info()[0])    
        
        db.rollback()
        return jsonify(message = 'Upvote failed'), 500

     return '', 204
