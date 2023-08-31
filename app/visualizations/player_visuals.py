import matplotlib.pyplot as plt

def create_player_ranking_plot(data):
    plt.figure(figsize=(10,5))
    plt.bar(data.keys(), data.values())
    plt.ylabel('Player Rank')
    plt.xlabel('Player Name')
    plt.title('Player Rankings')
    plt.tight_layout()
    plt.savefig('app/static/images/plot.png')
