import requests
import os
import json
from app.config import SLEEPER_BASE_URL, CACHE_DIR


def get_all_players(force_refresh=False):
    """Obtém todos os jogadores com cache"""
    cache_file = os.path.join(CACHE_DIR, 'players.json')

    if not force_refresh and os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            return json.load(f)

    url = f"{SLEEPER_BASE_URL}/players/nfl"
    response = requests.get(url)
    response.raise_for_status()
    players = response.json()

    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(cache_file, 'w') as f:
        json.dump(players, f)

    return players


def get_player(player_id):
    """Obtém dados de um jogador específico"""
    players = get_all_players()
    return players.get(str(player_id))