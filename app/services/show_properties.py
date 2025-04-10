from aiogram.types import Message
from sqlalchemy import select
from app.database.models import RealEstate
from app.database.session import SessionLocal

async def show_properties(message: Message, action: str):
    async with SessionLocal() as session:
        query = select(RealEstate).where(RealEstate.status == "available", RealEstate.type == action)
        result = await session.execute(query)
        properties = result.scalars().all()

        if not properties:
            await message.answer("Нет доступных вариантов.")
            return

        for estate in properties:
            text = (
                f"🏠 <b>{estate.title}</b>\n"
                f"📍 <b>Адрес:</b> {estate.address}\n"
                f"📐 <b>Площадь:</b> {estate.area} м²\n"
                f"💰 <b>Цена:</b> {estate.price:,.0f} ₽\n"
                f"👤 <b>Контакт:</b> {estate.contact_name}\n"
                f"📞 <b>Телефон:</b> {estate.contact_phone}"
            )
            await message.answer_photo(photo=estate.image_url, caption=text, parse_mode="HTML")
