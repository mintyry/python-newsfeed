# connects to database

from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

# loads env variables into python script
load_dotenv()

#connect to database using env variable

# getenv() is part of Python's built-in os module.
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(engine)

# returns a new session-connection object
# this fn means we can perform additional logic before creating db connection
# def get_db():
#     return Session()

# now this fn saves current connection on the g object, if it doesnt already exist.
def get_db():
    if 'db' not in g:
        #store db connection in app context
        g.db = Session()

    return g.db