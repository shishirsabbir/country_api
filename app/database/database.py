# imports
from app.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


# define engine
db_url: str = f"{settings.database_url}"  # need to update using pydantic settings
engine = create_async_engine(
    db_url,
)


# creating session using sessionmaker
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


# get db function
async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
