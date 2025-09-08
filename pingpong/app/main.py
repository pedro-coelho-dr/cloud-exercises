from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="PingPong")

class AuthMeIn(BaseModel):
    user: str

class AuthMeOut(BaseModel):
    user: str
    ping: str = "pong"

@app.post("/auth/me", response_model=AuthMeOut)
def auth_me(payload: AuthMeIn) -> AuthMeOut:
    return AuthMeOut(user=payload.user, ping="pong")