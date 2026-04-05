from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from database.CRUD import create_master_profile, get_user_id_by_tg_id, show_master_profile, published_master
from database.db import async_session_maker

from keyboards.reply_kb import get_after_rewrite_profile_keyboard

router = Router()

class ProfileForm(StatesGroup):
    name = State()           
    experience = State()     
    genre_games = State()    
    types_trpg = State()     
    description = State()
@router.message(lambda msg: msg.text == "Опубликовать")
async def set_to_public(msg: Message):
    tg_id = msg.from_user.id
    async with async_session_maker() as session:
        user_id = await get_user_id_by_tg_id(session, tg_id)
        await published_master(session, user_id)
@router.message(lambda msg: msg.text == "Создать анкету мастера")
async def edit_master_handler(msg: Message, state: FSMContext):
    await state.set_state(ProfileForm.name)
    await msg.reply('Введите ваше имя:')

@router.message(ProfileForm.name)
async def set_name(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(ProfileForm.experience)
    await msg.reply('Введите ваш опыт')
    
@router.message(ProfileForm.experience)
async def set_experience(msg: Message, state: FSMContext):
    await state.update_data(experience=msg.text)
    await state.set_state(ProfileForm.genre_games)
    await msg.reply('Введите ваши жанры игр')
    
@router.message(ProfileForm.genre_games)
async def set_genre(msg: Message, state: FSMContext):
    await state.update_data(genre_games=msg.text)
    await state.set_state(ProfileForm.types_trpg)
    await msg.reply('Введите НРИ которые вы играете')
    
@router.message(ProfileForm.types_trpg)
async def set_TRPG(msg: Message, state: FSMContext):
    await state.update_data(types_trpg=msg.text)
    await state.set_state(ProfileForm.description)
    await msg.reply('Опишите себя')

@router.message(ProfileForm.description)
async def set_description(msg: Message, state: FSMContext):
    await state.update_data(description=msg.text)
    data = await state.get_data()
    
    name = data.get('name')
    xp = data.get('experience')
    g_g = data.get('genre_games')
    t_g = data.get('types_trpg')
    description = data.get('description')
    await state.clear()
    tg_id = msg.from_user.id
    
    
    async with async_session_maker() as session:
        user_id = await get_user_id_by_tg_id(session, tg_id)
        await create_master_profile(session, user_id, name, xp, g_g, t_g, description)
        profile = await show_master_profile(session, user_id, user_id)
        
    await msg.reply(f'Вот ваша анкета:\n{profile}\nОпубликовать?', reply_markup=get_after_rewrite_profile_keyboard())
    
    
