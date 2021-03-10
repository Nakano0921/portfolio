from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin

from portfolio import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return Restaurant.query.get(user_id)

class Restaurant(UserMixin, db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    restaurant = db.Column(db.String(30), index=True)
    password = db.Column(db.String(30))

    def __init__(self, email, restaurant, password):
        self.email = email
        self.restaurant = restaurant
        self.password = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password, password)

    def add_user(self):
        with db.session.begin(subtransactions=True):
            db.session.add(self)
        db.session.commit()
    
    @classmethod
    def select_by_email(cls, email):
        return cls.query.filter_by(email=email).first()