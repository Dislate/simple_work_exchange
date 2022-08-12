from repositories.users import UserRepository
from db.base import db


def get_user_repository():
    return UserRepository(db)

