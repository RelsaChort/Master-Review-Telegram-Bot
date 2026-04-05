from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from database.db import async_session_maker

from keyboards.reply_kb import get_main_keyboard

router = Router()

@router.message(lambda msg: msg.text == "Вернуться в главное меню")
async def give_my_profile(msg: types.Message):
    await msg.answer("Возвращаю вас в главное меню.", reply_markup=get_main_keyboard())