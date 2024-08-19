from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, default="")
    price = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)
    
    def __init__ (self, name, image="", price=0.00):
        self.name = name
        self.image = image
        self.price = price
