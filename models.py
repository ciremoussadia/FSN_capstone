
import os
from sqlalchemy import Column, String, Integer, DateTime
from flask_sqlalchemy import SQLAlchemy

database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()

def setup_db(app, database_path=database_path):
  app.config['SQLALCHEMY_DATABASE_URI'] = database_path
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.app = app
  db.init_app(app)


actors_movies = db.Table('actors_movies',
                         db.Column('actor_id', db.Integer, db.ForeignKey(
                             'actor.id'), primary_key=True),
                         db.Column('movie_id', db.Integer, db.ForeignKey(
                             'movie.id'), primary_key=True)
                         )

class Movie(db.Model):
  id = Column(Integer, primary_key=True)
  title = Column(String, unique=True, nullable=False)
  release = Column(DateTime, nullable=False)
  actors = db.relationship('Actor', secondary=actors_movies,
                           lazy='subquery', backref=db.backref('movies'))

class Actor(db.Model):
  id = Column(Integer, primary_key=True)
  name = Column(String, unique=True, nullable=False)
  age = Column(String, nullable=False)
  gender = Column(String, nullable=False)
