# Simple auth dependency placeholder
from fastapi import Depends, HTTPException, status

async def get_current_user():
    # TODO: implement real auth (JWT/OAuth2)
    return {"id": 1, "name": "dev"}
