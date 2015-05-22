from model import *


class Role(Model, db.Model):
    __tablename__ = 'roles'

    name = db.Column(db.String(50), default="user", nullable=False)