from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.config import load_config

from sqlalchemy.orm import DeclarativeBase

config = load_config()
DATABASE_URL = config.db_url

engine = create_async_engine(DATABASE_URL, echo=False)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

