import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    phone = Column(String(250), nullable=False)
    photo = Column(String(250), nullable=False)

    publication = relationship("Publication", back_populates="user")
    comment = relationship("Comment", back_populates="user")

class Publication(Base):
    __tablename__ = 'publication'
    id = Column(Integer, primary_key=True)
    publication_type_id = Column(Integer, ForeignKey('publication_type.id'))
    title = Column(String(250), nullable=False)
    media = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="publication")
    publication_type = relationship("Publication_Type", back_populates="publication")
    comment = relationship("Comment", back_populates="publication")

class Publication_Type(Base):
    __tablename__ = 'publication_type'
    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=False)

    publication = relationship("Publication", back_populates="publication_type")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    publication_id = Column(Integer, ForeignKey('publication.id'))

    user = relationship("User", back_populates="comment")
    publication = relationship("Publication", back_populates="comment")

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
