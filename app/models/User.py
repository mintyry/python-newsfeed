# creates user class that inherits from Base
from app.db import Base
# these classes will define table columns and data types
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
# we want to use the bcrypt module directly
import bcrypt


salt = bcrypt.gensalt()
# Base class will use properties here to make the table
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
#   nulable false is an option that means NOT NULL
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

# add new validate_email method that is wrapped by @validate
  @validates('email')
#   this method returns what the value of the email column should be, and the @validates decorator internally handles the rest
  def validate_email(self, key, email):
    #make sure email address contains @ character
    # assert keyword is used to check if email addy contains @
    assert '@' in email

    return email
  
  @validates('password')
  def validate_password(self, key, password):
    # checks if password is more than 4 chars
    assert len(password) > 4

# validate_password() now returns an encrypted password if assert doesnt throw an error
    return bcrypt.hashpw(password.encode('utf-8'), salt)