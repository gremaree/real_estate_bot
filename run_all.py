import asyncio

async def main():
    # Шаг 1. Заполнение базы тестовыми данными
    print("Seeding database...")
    from scripts.seed import seed_data
    await seed_data()
    print("Seeding complete.")

    # Шаг 2. Запуск бота
    print("Starting bot...")
    from app.main import main as bot_main
    await bot_main()

if __name__ == '__main__':
    asyncio.run(main())
