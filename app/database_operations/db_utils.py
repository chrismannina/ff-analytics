from app.models import Player
from app import db

def add_player_to_db(name, rank):
    player = Player(name=name, rank=rank)
    db.session.add(player)
    db.session.commit()

def get_all_players():
    return Player.query.all()

# More utility functions as needed...
