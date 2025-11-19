from sqlalchemy import Numeric, String, create_engine
from sqlalchemy.orm import Session, sessionmaker, Mapped, mapped_column
from sqlalchemy.ext.asyncio import  async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

# local files
from api.db import config
from api.db import fields

engine = create_engine(
    url=config.SYNC_DB_URL,
    echo=True,
    pool_size=5
)

async_engine = create_async_engine(
    url=config.DB_URL_ASYNC,
    echo = True,
    pool_size = 5
)

SyncSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id: Mapped[fields.intpk]