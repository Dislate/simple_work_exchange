from fastapi import APIRouter, Depends, HTTPException, status
from models.tokens import Token, Login
from repositories.users import UserRepository
from endpoints.depends import get_user_repository
from core.security import verify_password, create_access_token

router_auth = APIRouter()


@router_auth.post("/", response_model=Token)
async def login(
        login: Login,
        users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_email(login.email)
    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")

    return Token(
        access_token=create_access_token({"sub": login.email}),
        token_type="Bearer",
    )
