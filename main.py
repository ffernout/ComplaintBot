import asyncio
from bot_config import dp, Bot

from hendlers.start import start_router
from hendlers.dialogue import review_button

async def main():
    dp.include_router(start_router)
    dp.include_router(review_button)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())