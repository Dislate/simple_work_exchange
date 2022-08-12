from typing import List
from fastapi import APIRouter, Depends
from repositories.users import UserRepository
from models.users import User, UserIn
from endpoints.depends import get_user_repository

router = APIRouter()


@router.get("/", response_model=List[User])
async def read_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 0):
    return await users.get_all(limit=limit, skip=skip)


@router.post("/create", response_model=User)
async def create_user(
        user: UserIn,
        users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)

# TODO: add update's, read_by_id's, delete's routes
