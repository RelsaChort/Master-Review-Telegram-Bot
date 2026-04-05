from aiogram import Dispatcher
from . import start, edit_master, edit_review, moderation, my_profile, back_to_menu, find_master

def register_all_handlers(dp: Dispatcher):
    dp.include_router(start.router)
    dp.include_router(my_profile.router)
    dp.include_router(back_to_menu.router)
    dp.include_router(edit_master.router)
    dp.include_router(find_master.router)
    # dp.include_router(edit_review.router)
    # dp.include_router(moderation.router)