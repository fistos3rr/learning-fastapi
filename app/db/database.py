from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase


class Database:
    def __init__(self, url: str, echo: bool = False) -> None:
        self.engine = create_async_engine(url, echo=echo, pool_pre_ping=True)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
    
    async def close(self) -> None:
        await self.engine.dispose()

class Base(DeclarativeBase):
    pass