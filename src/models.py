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
    fullname = Column(String(250), nullable=False)
    email= Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

class Planets (Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nulllable=False)
    climate = Column(String(20))
    diametro = Column(Integer(20))
    terreno = Column (String(20))
    url = Column (String(20))

class Character (Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nulllable=False)
    films = Column(String(20))
    gener = Column(Integer(20))
    eye_colour = Column (String(20))
    spwecies = Column (String(20))
    movies = Column(String(20))

class Characters_Favourites (Base):
    __tablename__ = 'characters_favourites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer(50), nulllable=False)
    character_id = Column(Integer(20), nulllable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

class Planets_Favourites (Base):
    __tablename__ = 'planets_favourites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer(50), nulllable=False)
    character_id = Column(Integer(20), nulllable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    
    

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
