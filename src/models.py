import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    fecha_subscripcion = Column(DateTime, default=datetime.utcnow)
    nombre = Column(String(250))
    apellido = Column(String(250))

    favoritos = relationship('Favorito', back_populates='usuario')

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    descripcion = Column(String(500))
  
    favoritos = relationship('Favorito', back_populates='planeta')

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    descripcion = Column(String(500))

    favoritos = relationship('Favorito', back_populates='personaje')

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'))
    personaje_id = Column(Integer, ForeignKey('personaje.id'))


    usuario = relationship('Usuario', back_populates='favoritos')

    planeta = relationship('Planeta', back_populates='favoritos')

    personaje = relationship('Personaje', back_populates='favoritos')

# Genera el diagrama.png utilizando el comando `$ python src/models.py`
render_er(Base, 'diagram.png')


