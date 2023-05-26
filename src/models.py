import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email= Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    subscription_date = Column(String(50), nullable=False)

class Planets(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nulllable=False)
    climate = Column(String(20))
    diametro = Column(Integer)
    terreno = Column (String(20))
    url = Column (String(20))

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nulllable=False)
    gender = Column(Integer(20))
    eye_colour = Column (String(20))
    species = Column (String(20))
    movies = Column(String(20))

class Characters_Favorites(Base):
    __tablename__ = 'characters_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer(50), ForeignKey('user.id'))
    character_id = Column(Integer(20), ForeignKey('character.id'))

class Planets_Favourites(Base):
    __tablename__ = 'planets_favourites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer(50), ForeignKey('user.id'))
    planet_id = Column(Integer(20), ForeignKey('planet.id'))
    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
