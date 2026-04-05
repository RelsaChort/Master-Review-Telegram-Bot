"""Create, Read, Update, Delete"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User, Master

async def get_or_create_user(session: AsyncSession, tg_id: int, username: str, first_name: str) -> User:
    result = await session.execute(select(User).where(User.tg_id == tg_id))
    user = result.scalar_one_or_none()
    if user is None:
        user = User(tg_id=tg_id, username=username, first_name=first_name)
        session.add(user)
        await session.commit()
        await session.refresh(user)
    return user

async def create_master_profile(
    session: AsyncSession, 
    user_id: int, 
    name: str, 
    experience: str, 
    genre_games: str, 
    types_TRPG: str, 
    description: str
    ) -> Master:
    stmt = select(Master).where(Master.user_id == user_id)
    result = await session.execute(stmt)
    profile = result.scalar_one_or_none()
    
    if profile:
        profile.name = name
        profile.experience = experience
        profile.genre_games = genre_games
        profile.types_TRPG = types_TRPG
        profile.description = description
        profile.is_published = False
        await session.commit()
        await session.refresh(profile)
        return profile
    else:
        profile = Master(
            user_id=user_id,
            name=name,
            experience=experience,
            genre_games=genre_games,
            types_TRPG=types_TRPG,
            description=description,
            is_published=False
        )
        session.add(profile)
        await session.commit()
        await session.refresh(profile)
        return profile

async def published_master(session: AsyncSession, user_id: int):
    profile = await session.get(Master, user_id)
    if profile:
        profile.is_published = True
        await session.commit()

async def show_master_profile(session: AsyncSession, user_id: int, user: int):
    stmt = select(Master).where(Master.user_id == user_id)
    result = await session.execute(stmt)
    profile = result.scalar_one_or_none()
    if not profile:
        return 'Анкета не найдена'
    if profile.is_published or profile.user_id == user:  #and profile.is_published
        lines = []
        fields = [
            ("ID", profile.user_id),
            ("Имя", profile.name),
            ("Рейтинг", profile.rating),
            ("Опыт", profile.experience),
            ("Жанры", profile.genre_games),
            ("НРИ", profile.types_TRPG),
            ("Описание", profile.description),
        ]
        for label, value in fields:
            if value and str(value).strip():
                lines.append(f'{label}: {value}')
            
        return '\n'.join(lines)
    return "Профиль не опубликован."
    
async def get_user_id_by_tg_id(session, tg_id: int) -> int | None:
    stmt = select(User.id).where(User.tg_id == tg_id)
    res = await session.execute(stmt)
    return res.scalar_one_or_none()