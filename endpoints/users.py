from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from repositories.users import UserRepository
from models.users import User, UserIn, UserResponse
from endpoints.depends import get_user_repository, get_current_user_repository

router = APIRouter()


@router.get("/", response_model=List[UserResponse])
async def read_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 0):
    return await users.get_all(limit=limit, skip=skip)


@router.post("/create", response_model=UserResponse)
async def create_user(
        user: UserIn,
        users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)


@router.put("/", response_model=UserResponse)
async def update_user(
        id: int,
        user: UserIn,
        users: UserRepository = Depends(get_user_repository),
        current_user: User = Depends(get_current_user_repository)):
    cur_user = await users.get_by_id(id=id)
    if user is None or user.email != current_user.email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    return await users.update(id=id, u=user)

# TODO: add read_by_id's, deletes routes
