from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from app.config import load_config
from app.handlers import common
from app.handlers import browser

async def main():
    config = load_config()
    bot = Bot(token=config.bot_token)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(common.router)
    await dp.start_polling(bot)

    dp.include_router(browser.router)
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
