from aiogram import Dispatcher
from . import start, edit_master, edit_review, moderation

def register_all_handlers(dp: Dispatcher):
    dp.include_router(start.router)
    # dp.include_router(edit_master.router)
    # dp.include_router(edit_review.router)
    # dp.include_router(moderation.router)