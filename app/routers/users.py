from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
async def create_user():
    pass


@router.get("/")
async def read_users():
    pass


@router.get("/{user_id}")
async def read_user_by_id():
    pass


@router.patch("/{user_id}")
async def update_user():
    pass


@router.delete("/{user_id}")
async def delete_user_by_id():
    pass
