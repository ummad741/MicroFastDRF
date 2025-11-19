from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
#local files
from api.db.models.user import UserTable
from api.schemas.user import UserCreateSchema
from api.db.deps import get_db

router = APIRouter()

@router.get("/users")
async def get_all_users(db: AsyncSession = Depends(get_db)):
    stmt = select(UserTable)
    result = await db.execute(stmt)
    return result.scalars().all()

@router.post("/users")
async def create_user(user: UserCreateSchema ,db: AsyncSession = Depends(get_db)):
    new_user = UserTable(
        name = user.name,
        age = user.age
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return "succsessfuly created"