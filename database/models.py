from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
    
class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, ForeignKey('masters.id', ondelete='CASCADE'))
    author_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    rating = Column(Integer)
    text = Column(Text)
    is_published = Column(Boolean, default=False)
    
    master = relationship("Master", back_populates="reviews")
    author = relationship("User", back_populates="reviews")
    
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, unique=True, nullable=False)
    username = Column(String)
    first_name = Column(String)
    is_admin = Column(Boolean, default=False)
    
    master_profile = relationship("Master", back_populates="user", uselist=False)
    reviews = relationship("Review", back_populates="author")
    
    
class Master(Base):
    __tablename__ = 'masters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), unique=True)
    name = Column(String, nullable=False)
    rating = Column(String)
    experience = Column(Text)
    genre_games = Column(Text)
    types_TRPG = Column(Text)
    description = Column(Text)
    is_published = Column(Boolean, default=False)
    
    user = relationship("User", back_populates="master_profile")
    reviews = relationship("Review", back_populates="master", cascade="all, delete-orphan")