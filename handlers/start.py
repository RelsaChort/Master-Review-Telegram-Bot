from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from database.CRUD import get_or_create_user
from database.db import async_session_maker

from keyboards.reply_kb import get_main_keyboard
router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    async with async_session_maker() as session:
        user = await get_or_create_user(
            session,
            tg_id=msg.from_user.id,
            username=msg.from_user.username,
            first_name=msg.from_user.first_name
        )
    await msg.answer(f"Добро пожаловать, {msg.from_user.first_name}! Выберете действие", reply_markup=get_main_keyboard())
