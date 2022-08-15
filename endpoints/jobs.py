from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from repositories.jobs import JobRepository
from models.jobs import Job, JobIn
from models.users import User
from endpoints.depends import get_jobs_repository, get_current_user_repository

router_jobs = APIRouter()


@router_jobs.get("/", response_model=List[Job])
async def read_jobs(
        limit: int = 100,
        skip: int = 0,
        jobs: JobRepository = Depends(get_jobs_repository)):
    return await jobs.get_all(limit=limit, skip=skip)


@router_jobs.post("/", response_model=Job)
async def create_jobs(
        j: JobIn,
        jobs: JobRepository = Depends(get_jobs_repository),
        current_user: User = Depends(get_current_user_repository)):
    return await jobs.create(user_id=current_user.id, j=j)


@router_jobs.put("/", response_model=Job)
async def update_jobs(
        id: int,
        j: JobIn,
        jobs: JobRepository = Depends(get_jobs_repository),
        current_user: User = Depends(get_current_user_repository)):
    job = await jobs.get_by_id(id=id)
    if job is None or job.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return await jobs.update(id=id, user_id=current_user.id, j=j)


@router_jobs.delete("/")
async def delete_jobs(
        id: int,
        jobs: JobRepository = Depends(get_jobs_repository),
        current_user: User = Depends(get_current_user_repository)):
    exp = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    job = await jobs.get_by_id(id=id)
    if job is None or job.user_id != current_user.id:
        raise exp
    await jobs.delete(id=id)
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
