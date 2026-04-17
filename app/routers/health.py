from typing import Annotated, Any

from fastapi import APIRouter, Depends

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db_session


router = APIRouter(prefix="/health", tags=["health"])


@router.get("/db")
async def health_check(
    db: Annotated[AsyncSession, Depends(get_db_session)],
) -> Any:
    try:
        result = await db.execute(text("SELECT version();"))
        db_version = result.scalars().one()
        return {"status": "healthy", "db_version": db_version}
    except SQLAlchemyError:
        return {"status": "unhealthy"}
