import logging.config
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Annotated

from fastapi import FastAPI, Depends, HTTPException

from app.routers import users, health
from app.core.config import LOGGING_CONFIG, settings
from app.db.database import sessionmanager, get_db_session

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("app")

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    if sessionmanager._engine is not None:
        await sessionmanager.close()

app = FastAPI(lifespan=lifespan)

app.include_router(health.router)
app.include_router(users.router)