from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Union

class Settings(BaseSettings):
    app_name: str = "Buda Iphone Shop"
    debug: bool = True
    database_url: str = "postgresql+asyncpg://postgres:1337@localhost:5432/IphoneBuda"
    cors_origins: Union[List[str], str] = [
        "http://localhost:5173",
        "http://localhost:8000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:8000",
    ]
    static_dir: str = "static"
    images_dir: str = "static/images"

    model_config =  SettingsConfigDict(
        env_file = ".env"
    )

settings = Settings()