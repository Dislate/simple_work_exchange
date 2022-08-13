from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from core.config import ACCESS_TOKEN_EXPIRE_MINUTE, ALGORITHM, SECRET_KEY

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashpsw: str) -> bool:
    return pwd_context.verify(password, hashpsw)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)})
    print(to_encode)
    return jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):
    try:
        encoded_jwt = jwt.decode(token, key=SECRET_KEY, algorithms=ALGORITHM)
    except jwt.JWTError:
        return None
    return encoded_jwt
