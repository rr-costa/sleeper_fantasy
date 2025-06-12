# app/__init__.py
"""
Pacote principal da aplicação Sleeper Fantasy
Módulos:
- api: Integração com a Sleeper API
- services: Lógica de negócios e análises
- utils: Funções auxiliares
"""
from .api import get_user
# Exportações principais
from .api.league import get_league, get_rosters, get_users, get_user_leagues
from .api.user import get_user
from .api.players import get_player, get_all_players
from .services.team_analysis import (
    get_user_team,
    get_team_scores,
    compare_teams
)

# Atalhos úteis
from .config import SLEEPER_BASE_URL, SPORT, SEASON

# Lista de exportações para 'from app import *'
__all__ = [
    'get_league',
    'get_rosters',
    'get_users',
    'get_user',
    'get_user_leagues',
    'get_player',
    'get_all_players',
    'get_user_team',
    'get_team_scores',
    'compare_teams',
    'SLEEPER_BASE_URL',
    'SPORT',
    'SEASON'
]