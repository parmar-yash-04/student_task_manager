from pydantic_settings import BaseSettings
import os

ENV = os.getenv("ENV", "dev")
ENV_FILE = ".env.dev" if ENV == "dev" else ".env.prod"

class Settings(BaseSettings):
    # database_hostname: str
    # database_port: int
    # database_username: str
    # database_password: str
    # database_name: str
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    env: str = "dev"

    class Config:
        env_file = ENV_FILE

settings = Settings()