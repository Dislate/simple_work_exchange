from datetime import datetime
from typing import List, Optional
from db.users import users
from core.security import hash_password
from repositories.base import BaseRepository
from models.users import User, UserIn, UserResponse


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[UserResponse]:
        query = users.select().limit(limit).offset(skip)
        return await self.db.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[UserResponse]:
        query = users.select().where(users.c.id == id)
        user = await self.db.fetch_one(query)
        if user is None:
            return None
        return UserResponse.parse_obj(user)

    async def create(self, u: UserIn) -> User:
        user = User(
            user_id=0,
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop("id", None)
        query = users.insert().values(**values)
        user.id = await self.db.execute(query)
        return user

    async def update(self, id: int, u: UserIn) -> User:
        user = User(
            id=id,
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            updated_at=datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop("created_at", None)
        values.pop("id", None)
        query = users.update().where(users.c.id == id).values(**values)
        await self.db.execute(query)
        return user

    async def get_by_email(self, email: str) -> UserResponse:
        query = users.select().where(users.c.email == email)
        user = await self.db.fetch_one(query)
        if user is None:
            return None
        return user
