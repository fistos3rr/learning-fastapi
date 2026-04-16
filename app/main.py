import logging.config
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.routers import users
from app.core.config import LOGGING_CONFIG, get_settings

settings = get_settings()

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("app")
        

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
    
app.include_router(users.router)