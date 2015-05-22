import flask.ext.sqlalchemy

db = flask.ext.sqlalchemy.SQLAlchemy()

class Model(object):
    """
    Model
    **Overview**

    Used to generalize attributes and methods for all models package.
    """
    id = db.Column(db.Integer, primary_key=True)