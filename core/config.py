from pydantic import BaseModel
from pydantic_settings import BaseSettings

DB_PATH = "my_database.db"


class DbSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = True


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db: DbSettings = DbSettings()


settings = Settings()
