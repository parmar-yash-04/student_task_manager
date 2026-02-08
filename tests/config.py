from pydantic_settings import BaseSettings, SettingsConfigDict

class TestSettings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    env: str = "test"

    model_config = SettingsConfigDict(env_file=".env.test")

test_settings = TestSettings()