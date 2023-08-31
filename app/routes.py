from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/player_data')
def player_data():
    # In a real implementation, you'd fetch player data and tiers here
    return render_template('player_data.html', players=[], tiers=[])
