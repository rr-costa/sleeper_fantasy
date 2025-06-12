import requests
from app.config import SLEEPER_BASE_URL

def get_user(username: str):
    """Obtém informações básicas da liga"""
    url = f"{SLEEPER_BASE_URL}/user/{username}"
    response = requests.get(url)
    response.raise_for_status()

    user_data = response.json()

    if not user_data or "user_id" not in user_data:
        raise ValueError(f"Usuário '{username}' não encontrado na API da Sleeper.")

    return user_data