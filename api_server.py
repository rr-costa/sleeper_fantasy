# api_server.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app import get_user, get_user_leagues

app = FastAPI()

# Permitir que o Angular (rodando em http://localhost:4200) acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/user/{username}")
def validate_user(username: str):
    try:
        user_data = get_user(username)
        return user_data
    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")

@app.get("/api/leagues/{username}")
def get_leagues(username: str):
    try:
        user_data = get_user(username)
        user_id = user_data["user_id"]
        leagues = get_user_leagues(user_id)
        return leagues
    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")

# Rodar manualmente com: python api_server.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_server:app", host="0.0.0.0", port=8000, reload=True)
