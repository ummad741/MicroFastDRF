from fastapi import FastAPI, Depends
from api.routers.user import router as user_router
app = FastAPI()

app.include_router(user_router)