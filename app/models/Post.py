from datetime import datetime
from app.db import Base
# Need to import Vote so SQLAlchemy can know about it when running the select line/sql queries
# The User and COmment models will be resolved when the app runs and models are being used; strings are enough
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

# making post model
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship('User')
    comments = relationship('Comment', cascade='all,delete')
    votes = relationship('Vote', cascade='all,delete')
    
    # when querying this model, this property will perform a select with the sqlalchemy func.count() to add up the votes
# INCORRECT PROVIDED BY INSTRUX
    # vote_count = column_property(
    #     select([func.count(Vote.id)]).where(Vote.post_id == lambda: Post.id)
    # )

# property decorator dictates that vote_count is a property of Post model
    @property
    def vote_count(self):
        # calculates no of votes by returning the length of votes on this post
        return len(self.votes)
    
    