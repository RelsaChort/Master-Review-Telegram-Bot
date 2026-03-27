import asyncio
import logging

import config
from handlers import register_all_handlers

from aiohttp import ClientSession, TCPConnector

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties 
async def main():
    connector = TCPConnector()
    # proxy = "socks5://127.0.0.1:1080"
    # session = ClientSession(connector=connector)
    bot = Bot(
        token=config.BOT_TOKEN, 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        # session=session,
        # proxy=proxy
        )
    dp = Dispatcher(storage=MemoryStorage())
    register_all_handlers(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
