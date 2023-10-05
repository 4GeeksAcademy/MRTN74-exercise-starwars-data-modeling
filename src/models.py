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
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))
    birth_year = Column(Integer)
    gender = Column(String(20))

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(50))
    terrain = Column(String(50))
    population = Column(Integer)
    diameter = Column(Integer)

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    crew = Column(Integer) 
    passengers = Column(Integer) 
    cargo_capacity = Column(Integer) 
    consumables = Column(String(50))
    hyperdrive_rating = Column(Integer)
    starship_class = Column(String(50))
    pilots = Column(String(50))

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship(User)
    character = relationship(Character)

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship(User)
    planet = relationship(Planet)

class FavoriteStarship(Base):
    __tablename__ = 'favorite_starship'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    starship_id = Column(Integer, ForeignKey('starship.id'))
    user = relationship(User)
    starship = relationship(Starship)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
