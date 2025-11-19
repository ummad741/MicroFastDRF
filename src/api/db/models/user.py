from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    String, Boolean, Integer, Column
)
from api.db.connection import BaseModel


class UserTable(BaseModel):
    __tablename__ = "user_user"
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer)
