# ~/sleeper_fantasy/main.py
from app import get_user,get_user_leagues

def main():
    # 1. Obter IDs de usuários
    username = "saopaulojets"
    try:
        user_data = get_user(username)
        user_id = user_data["user_id"]

        leagues = get_user_leagues(user_id)

        print(f"{username} participa de {len(leagues)} liga(s):")

        for league in leagues:
            print(f"- {league['name']} (ID: {league['league_id']})")

    except ValueError as ve:
        print(f"[ERRO]: {ve}")
    except Exception as e:
        print(f"[ERRO INESPERADO]: {e}")


if __name__ == "__main__":
    main()