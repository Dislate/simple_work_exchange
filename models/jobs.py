import datetime
from typing import Optional
from pydantic import BaseModel


class BaseJob(BaseModel):
    title: str
    description: str
    salary_from: int
    salary_to: int
    is_active: bool = True


class Job(BaseJob):
    id: Optional[int] = None
    user_id: int
    created_at: Optional[datetime.datetime]
    updated_at: datetime.datetime


class JobIn(BaseJob):
    pass
