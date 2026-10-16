from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from backend.app.config import settings

engine = create_async_engine(
    settings.database_url
)

new_session = async_sessionmaker(engine,autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = new_session()
    try:
        yield db
    finally:
        db.close()

async def create_tables():
    async with engine.begin() as conn:
        await  conn.run_sync(Base.metadata.drop_all)
        await  conn.run_sync(Base.metadata.create_all)