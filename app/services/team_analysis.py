from app import get_rosters, get_users
from app import get_player
from ..api import get_weekly_matchups

def compare_teams(user_id, opponent_id):
    """Compara dois times"""
    user_team = get_user_team(user_id)
    opponent_team = get_user_team(opponent_id)

    if not user_team or not opponent_team:
        return None

    comparison = {}
    positions = ['QB', 'RB', 'WR', 'TE', 'DEF', 'K']  # Posições padrão

    for pos in positions:
        user_players = [p for p in user_team['starters'] if p and p['position'] == pos]
        opp_players = [p for p in opponent_team['starters'] if p and p['position'] == pos]

        comparison[pos] = {
            "user_players": [p['full_name'] for p in user_players],
            "opponent_players": [p['full_name'] for p in opp_players]
        }

    return comparison

def get_team_scores(user_id):
    """Retorna histórico de pontuações do time por semana"""
    rosters = get_rosters()
    user_roster = next((r for r in rosters if r['owner_id'] == user_id), None)

    if not user_roster:
        return None

    scores = {}
    for week in range(1, 19):  # Temporada regular NFL
        try:
            matchups = get_weekly_matchups(week)
            team_score = next((m['points'] for m in matchups if m['roster_id'] == user_roster['roster_id']), 0)
            scores[f"Week {week}"] = team_score
        except:
            continue
    return scores

def get_user_team(user_id):
    """Retorna o time completo de um usuário"""
    rosters = get_rosters()
    user_roster = next((r for r in rosters if r['owner_id'] == user_id), None)

    if not user_roster:
        return None

    return {
        "starters": [get_player(p_id) for p_id in user_roster['starters']],
        "reserves": [get_player(p_id) for p_id in user_roster['reserve']]
    }