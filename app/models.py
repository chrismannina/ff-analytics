from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    # Add other fields as necessary
