import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from db import init_db

# Handlers
from handlers import (
    start,
    upload,
    pending,
    admin_panel,
    broadcast,
    modlog,
    inline_search   # 🔎 Inline search qo‘shildi
)

async def main():
    # DB init
    await init_db()

    # Bot va Dispatcher
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Routers ulash
    dp.include_router(start.router)
    dp.include_router(upload.router)
    dp.include_router(pending.router)
    dp.include_router(admin_panel.router)
    dp.include_router(broadcast.router)
    dp.include_router(modlog.router)
    dp.include_router(inline_search.router)  # 🔎 Inline search

    print("✅ Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())