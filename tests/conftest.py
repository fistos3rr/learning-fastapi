import pytest
import httpx
from app.main import app

@pytest.fixture
async def client():
    """Async client for FastAPI Tests"""
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://localhost:8080"
    ) as c:
        yield c
