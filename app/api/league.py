import requests
from app.config import SLEEPER_BASE_URL, SPORT, SEASON

def get_user_leagues(user_id: str):
    """Obtém informações básicas da liga"""
    url = f"{SLEEPER_BASE_URL}/user/{user_id}/leagues/{SPORT}/{SEASON}"
    print(url)
    response = requests.get(url)
    response.raise_for_status()

    leagues = response.json()

    if not leagues:
        raise ValueError(f"O usuário '{user_id}' não participa de nenhuma liga em {SEASON} ).")

    return leagues

def get_league():
    """Obtém informações básicas da liga"""
    url = f"{SLEEPER_BASE_URL}/league/LEAGUE_ID"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_rosters():
    """Obtém todos os times da liga"""
    url = f"{SLEEPER_BASE_URL}/league/LEAGUE_ID/rosters"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_users():
    """Obtém informações dos usuários"""
    url = f"{SLEEPER_BASE_URL}/league/LEAGUE_ID/users"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()