from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from database.CRUD import show_master_profile, get_user_id_by_tg_id
from database.db import async_session_maker

from keyboards.reply_kb import get_my_profile_keyboard_1
router = Router()

@router.message(lambda msg: msg.text == 'Моя анкета')
async def give_my_profile(msg: types.Message):
    async with async_session_maker() as session:
        user_id = await get_user_id_by_tg_id(session, msg.from_user.id)
        if user_id is None:
            await msg.answer("Ошибка: вы не зарегистрированы.")
            return
        my_profile = await show_master_profile(session, user_id)
        if my_profile:
            await msg.answer(my_profile)
        else:
            await msg.answer("У вас отсутствует профиль мастера, хотите его сделать?", reply_markup=get_my_profile_keyboard_1())