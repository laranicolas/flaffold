from model import *


class User(Model, db.Model):
    __tablename__ = 'users'

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    area_code = db.Column(db.Integer)
    roles = db.relationship('Role', backref=db.backref('users', lazy='dynamic'))
