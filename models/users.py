from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, validator, constr


class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    hashed_password: str
    is_company: bool
    updated_at: datetime
    created_at: datetime


class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: constr(max_length=8)
    password_confirm: str
    is_company: bool = False

    @validator("password_confirm")
    def password_confirm(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("Password don't match")
        return v
