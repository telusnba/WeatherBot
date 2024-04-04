import asyncio

from Handlers import dp
from Handlers.AdminHandler import admin_message
from loader import bot


async def main() -> None:
    await admin_message()
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.run(main())
