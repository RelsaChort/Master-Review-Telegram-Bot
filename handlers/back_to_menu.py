from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from database.db import async_session_maker

from keyboards.reply_kb import get_main_keyboard

import msg_text

router = Router()

@router.message(lambda msg: msg.text == msg_text.back_to_menu)
async def back_to_main_menu(msg: types.Message):
    await msg.answer("Возвращаю вас в главное меню.", reply_markup=get_main_keyboard())