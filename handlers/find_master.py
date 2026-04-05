from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database.db import async_session_maker
from database.CRUD import show_master_profile, get_user_id_by_tg_id

from keyboards.reply_kb import get_main_keyboard

import msg_text
router = Router()

class FindMaster(StatesGroup):
    input_id = State()

@router.message(lambda msg: msg.text == msg_text.find_master)
async def find_master1(msg: types.Message, state: FSMContext):
    await state.set_state(FindMaster.input_id)
    await msg.reply("Введите ID мастера")
    
@router.message(FindMaster.input_id)
async def find_master2(msg: types.Message, state: FSMContext):
    await state.clear()
    msg_text = msg.text
    try:
        msg_text = int(msg_text)
        tg_user_id = msg.from_user.id
        async with async_session_maker() as session:
            user_id = await get_user_id_by_tg_id(session, tg_user_id)
            text = await show_master_profile(session, msg_text, user_id)
            if text:
                await msg.reply(text, reply_markup=get_main_keyboard())
    except:
        await msg.reply('Введите только ID', reply_markup=get_main_keyboard())