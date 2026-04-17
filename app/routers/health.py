from typing import Annotated

from fastapi import APIRouter, Depends

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db_session


router = APIRouter(prefix="/health", tags=["health"])


@router.get("/db")
async def health_check(
    db: Annotated[AsyncSession, Depends(get_db_session)],
):
    try:
        result = await db.execute(text("SELECT version();"))
        db_version = result.scalars().one()
        return {"status": "healthy", "db_version": db_version}
    except Exception:
        return {"status": "unhealthy"}
