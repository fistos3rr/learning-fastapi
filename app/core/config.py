import logging
import sys
from functools import lru_cache
from pydantic import (
    PostgresDsn,
    computed_field
)
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore"
    )
    
    DEBUG: bool = False
    
    PG_HOST: str
    PG_PORT: int = 5432
    PG_USER: str
    PG_PASSWORD: str = ""
    PG_DB: str = ""
    
    @computed_field
    @property
    def PG_DATABASE_URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.PG_USER,
            password=self.PG_PASSWORD,
            host=self.PG_HOST,
            port=self.PG_PORT,
            path=self.PG_DB
        )


@lru_cache
def settings() -> Settings:
    return Settings()

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "default",
            "stream": "ext://sys.stdout",
        },
        "file_handler": { 
            "formatter": "default",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "app.log",
            "maxBytes": 1024 * 1024 * 1, # = 1MB
            "backupCount": 3,
        },
    },
    
    "loggers": {
        "app": {"handlers": ["console", "file_handler"], "level": "DEBUG", "propagate": False},
    },
    #"root": {"handlers": ["console"], "level": "DEBUG"},
}

