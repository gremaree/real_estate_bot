from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from app.states.property import PropertyBrowsing
from sqlalchemy import select
from app.database.models import RealEstate
from app.database.session import SessionLocal

router = Router()

# Старт: аренда или покупка
@router.message(F.text == "/start")
async def start(message: Message, state: FSMContext):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏠 Купить", callback_data="type_buy")],
        [InlineKeyboardButton(text="📦 Арендовать", callback_data="type_rent")]
    ])
    await message.answer("Что вас интересует?", reply_markup=keyboard)

# Обработка выбора
@router.callback_query(F.data.startswith("type_"))
async def choose_type(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    selected_type = callback.data.split("_")[1]  # buy / rent
    await state.set_state(PropertyBrowsing.browsing)
    await state.update_data(index=0, type=selected_type)
    await show_property(callback.message, state)

# Переключение карточек
@router.callback_query(F.data.in_(["next", "prev"]))
async def navigate(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    index = data.get("index", 0)
    prop_type = data.get("type")

    index = index + 1 if callback.data == "next" else max(index - 1, 0)
    await state.update_data(index=index)
    await show_property(callback.message, state)

# Показ карточки
async def show_property(message: Message, state: FSMContext):
    data = await state.get_data()
    index = data.get("index", 0)
    prop_type = data.get("type")

    async with SessionLocal() as session:
        stmt = select(RealEstate).where(RealEstate.type == prop_type, RealEstate.status == "available")
        result = await session.execute(stmt)
        properties = result.scalars().all()

    if not properties:
        await message.answer("Объекты не найдены.")
        return

    if index >= len(properties):
        index = 0
        await state.update_data(index=0)

    prop = properties[index]
    caption = (
        f"<b>{prop.title}</b>\n"
        f"📍 {prop.address}\n"
        f"📐 {prop.area} м²\n"
        f"💰 {prop.price:,.0f} ₽\n"
        f"👤 {prop.contact_name} — {prop.contact_phone}"
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="prev"),
         InlineKeyboardButton(text="➡️ Следующий", callback_data="next")]
    ])

    await message.answer_photo(photo=prop.image_url, caption=caption, reply_markup=keyboard, parse_mode="HTML")
