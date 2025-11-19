from api.db.connection import AsyncSessionLocal

async def get_db():
    async with  AsyncSessionLocal() as session:
        yield session