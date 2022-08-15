from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, validator, constr


class BaseUser(BaseModel):
    name: str
    email: EmailStr
    is_company: bool


class UserResponse(BaseUser):
    id: Optional[int] = None
    updated_at: datetime
    created_at: Optional[datetime]


class User(UserResponse):
    hashed_password: str


class UserIn(BaseUser):
    password: constr(max_length=8)
    password2: str

    @validator("password2")
    def password_confirm(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("Password don't match")
        return v
