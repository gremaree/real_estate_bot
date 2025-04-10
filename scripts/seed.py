from app.database.session import SessionLocal
from app.database.models import RealEstate

# Обрати внимание — убрали asyncio.run
async def seed_data():
    async with SessionLocal() as session:
        properties = [
            RealEstate(
                type="buy",
                title="Современная квартира в центре",
                address="Москва, ул. Арбат, д. 10",
                area=48.5,
                price=13200000.0,
                contact_name="Анна Иванова",
                contact_phone="+7 999 123 45 67",
                image_url="https://upload.wikimedia.org/wikipedia/commons/6/65/Flat_example.jpg",
                status="available"
            ),
            RealEstate(
                type="rent",
                title="Уютная студия возле парка",
                address="Санкт-Петербург, ул. Ленина, д. 22",
                area=32.0,
                price=45000.0,
                contact_name="Игорь Петров",
                contact_phone="+7 900 888 77 66",
                image_url="https://upload.wikimedia.org/wikipedia/commons/e/e5/Studio_apartment.jpg",
                status="available"
            )
        ]
        session.add_all(properties)
        await session.commit()

# Только для ручного запуска файла напрямую
if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_data())
