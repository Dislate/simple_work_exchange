import datetime
from pydantic import BaseModel


class JobBase(BaseModel):
    title: str
    description: str
    salary_from: int
    salary_to: int
    is_active: bool = True


class Job(JobBase):
    id: int
    user_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


class JobIn(JobBase):
    pass
