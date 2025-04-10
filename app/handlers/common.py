from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

router = Router()

@router.message(F.text == "/start")
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Купить", callback_data="action_buy")],
        [InlineKeyboardButton(text="Арендовать", callback_data="action_rent")]
    ])
    await message.answer("Что вас интересует?", reply_markup=keyboard)

@router.callback_query(F.data.startswith("action_"))
async def handle_action(callback: CallbackQuery):
    action = callback.data.split("_")[1]
    from app.services.show_properties import show_properties
    await show_properties(callback.message, action)
