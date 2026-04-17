import logging.config
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.routers import users, health
from app.core.config import LOGGING_CONFIG
from app.db.database import sessionmanager

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("app")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    yield
    if sessionmanager._engine is not None:
        await sessionmanager.close()


app = FastAPI(lifespan=lifespan)

app.include_router(health.router)
app.include_router(users.router)
