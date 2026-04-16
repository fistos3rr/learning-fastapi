from fastapi import FastAPI, Request
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator


async def get_db_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    factory = request.app.state.db.session_factory

    async with factory() as session:
        try:
            yield session
            #await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()