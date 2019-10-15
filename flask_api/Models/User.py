from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property
from .Database import *

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    config_id = db.Column(unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(500), unique=True, nullable=False)
    email_confirmation_token = db.Column(unique=True, nullable=False)
    email_confirmed_at = db.Column(db.DateTime, nullable=True)
    password_reset_token = db.Column(unique=True, nullable=True)
    frequency_capping_enabled = db.Column(db.Boolean, default=True)
    max_frequency = db.Column(db.Integer, nullable=True)

    @hybrid_property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, p):
        self.password_hash = generate_password_hash(p)

    def chck_psswd(self, p):
        return check_password_hash(self.password_hash, p)

    def __repr__(self):
        return f'<Username {self.username}>'


# class UserSchema(ma.ModelSchema):
    
#     class Meta:
#         model = User

