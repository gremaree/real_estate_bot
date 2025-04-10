import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

from app.config import load_config 
from app.database.models import Base  

# конфиг логгирования
config = context.config
fileConfig(config.config_file_name)

# получаем URL из .env
config_obj = load_config()
config.set_main_option("sqlalchemy.url", config_obj.db_url)

target_metadata = Base.metadata



def run_migrations_offline():
    """Миграции в оффлайн-режиме (без подключения к БД)"""
    context.configure(
        url=config_obj.db_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Сама миграция — уже с подключением"""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Миграции в онлайн-режиме с asyncpg"""
    connectable = create_async_engine(
        config_obj.db_url,
        poolclass=pool.NullPool,
        future=True,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
