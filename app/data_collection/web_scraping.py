import requests
from bs4 import BeautifulSoup

def fetch_data_via_scraping():
    url = "https://www.fantasypros.com/nfl/rankings/consensus-cheatsheets.php"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Placeholder for the actual extraction logic
    players = [tag.get_text() for tag in soup.find_all('YOUR_TAG_FOR_PLAYERS')]
    
    return players
