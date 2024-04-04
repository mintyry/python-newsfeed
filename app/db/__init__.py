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

# passed in app so we can use teardown merthod; now we dont have to worry about connections remaining open and potentially locking up the server, and we dont have to put a db.close() at the end of every route
def init_db(app):
    Base.metadata.create_all(engine)
# Flask runs close_db with its teardown_appcontext method
    app.teardown_appcontext(close_db)

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

# This will not run auromatically though; need to tel Flas to run it whenever context is destroyed.
def close_db(e=None):
    db = g.pop('db', None)

# .pop() attemps to find and remove db from thew g object; if db exists (meaning, db does not equal None), then db.close() ends the connection.
    if db is not None:
        db.close()