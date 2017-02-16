"""Models and database functions"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Model definitions

class KilnData(db.Model):
  """KilnData"""
  __tablename__ = "KilnData"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  temperature = db.Column(db.Integer)
  updatedAt = db.Column(db.DateTime)

  def to_dict(self):
    result = {}
    for key in self.__mapper__.c.keys():
      result[key] = getattr(self, key)
    return result

# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use MySQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/KilnSitter'
    db.app = app
    db.init_app(app)
