import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
import enum
from sqlalchemy import Integer, Enum

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)


class GenderEnum(enum.Enum):
    male = 1
    female = 2
    not_specified = 3


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birth_year = Column(Integer)
    gender = Column(Enum(GenderEnum))
    height = Column(Integer)
    skin_color = Column(String(20), nullable=False)
    eye_color = Column(String(20), nullable=False)


class Fav_Character(Base):
    __tablename__ = 'fav_character'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    character_id = Column(Integer, ForeignKey(
        'character.id'), primary_key=True)
    user = relationship("User")
    character = relationship("Character")


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(20), nullable=False)
    gravity = Column(String(20), nullable=False)
    terrain = Column(String(50), nullable=False)
    surface_water = Column(Integer)
    population = Column(Integer)


class Fav_Planet(Base):
    __tablename__ = 'fav_planet'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), primary_key=True)
    user = relationship("User")
    character = relationship("Planet")

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
