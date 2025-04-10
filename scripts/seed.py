import asyncio
from app.database.models import RealEstate
from app.database.session import SessionLocal, engine, Base

async def seed():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with SessionLocal() as session:
        estate = RealEstate(
            type="buy",
            title="Уютная квартира в центре",
            address="Москва, ул. Арбат, д. 12",
            area=45.0,
            price=12500000.0,
            contact_name="Анна Иванова",
            contact_phone="+7 900 123 45 67",
            image_url="https://upload.wikimedia.org/wikipedia/commons/6/65/Flat_example.jpg",
            status="available"
        )
        session.add(estate)
        await session.commit()

asyncio.run(seed())
