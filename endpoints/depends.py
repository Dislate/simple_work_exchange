from fastapi import Depends, HTTPException, status
from repositories.users import UserRepository
from repositories.jobs import JobRepository
from db.base import db
from models.users import User
from core.security import JWTBearer, decode_access_token


def get_user_repository() -> UserRepository:
    return UserRepository(db)


def get_jobs_repository() -> JobRepository:
    return JobRepository(db)


async def get_current_user_repository(
        users: UserRepository = Depends(get_user_repository),
        token: str = Depends(JWTBearer())
) -> User:
    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid")
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception

    email: str = payload.get("sub")
    if email is None:
        raise cred_exception

    user = await users.get_by_email(email=email)
    user = User.parse_obj(user)
    if user is None:
        raise cred_exception

    return user
