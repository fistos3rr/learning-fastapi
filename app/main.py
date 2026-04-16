import logging.config
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Annotated

from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.routers import users
from app.core.config import LOGGING_CONFIG, settings
from app.db.database import Database
from app.dependencies import get_db_session

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("app")

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    db_instance = Database(
        url=str(settings().PG_DATABASE_URI),
        echo=True
    )
    app.state.db = db_instance
    yield
    await db_instance.close()

app = FastAPI(lifespan=lifespan)

@app.get("/health")
async def health_check(
    db: Annotated[AsyncSession, Depends(get_db_session)]
):
    try:
        result = await db.execute(text("SELECT version()"))
        db_version = result.scalar()
        return {"status": "healthy", "db_version": db_version}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB error: {str(e)}")
    
app.include_router(users.router)