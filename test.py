import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

async def test_db():
    engine = create_async_engine("postgresql+asyncpg://postgres:cats@localhost:5432/realestate_db")
    try:
        async with engine.begin() as conn:
            result = await conn.execute(text("SELECT 1"))
            print("✅ Подключение успешно:", result.scalar())
    except Exception as e:
        print("❌ Ошибка подключения:", e)

asyncio.run(test_db())
