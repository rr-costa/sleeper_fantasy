import requests
from app.config import SLEEPER_BASE_URL

def get_weekly_matchups(week):
    """Obtém confrontos e pontuações por semana"""
    url = f"{SLEEPER_BASE_URL}/league/{LEAGUE_ID}/matchups/{week}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()