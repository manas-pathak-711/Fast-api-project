from pydantic_settings import BaseSettings
from dotenv import load_dotenv


# Define the absolute path to the .env file
env_path = r"D:\Manas\Holiday-Study\Mini-Backend\main\.env"

# Explicitly load the .env file
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    DATABASE_HOSTNAME: str
    DATABASE_PORT: int
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = env_path  # Use the same absolute path here

settings = Settings()

