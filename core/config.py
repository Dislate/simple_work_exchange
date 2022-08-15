from starlette.config import Config


config = Config(".env_dev")

DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTE = 60
ALGORITHM = "HS256"
SECRET_KEY = config("SECRET_KEY", cast=str)
