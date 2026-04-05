from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import msg_text

back_to_menu =[KeyboardButton(text=msg_text.back_to_menu)]

def get_main_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text=msg_text.find_master)],
        [KeyboardButton(text=msg_text.create_master_profile)],
        [KeyboardButton(text=msg_text.my_profile)]
    ]
    kb = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return kb

def get_my_profile_keyboard_1() -> ReplyKeyboardMarkup:
    '''клавиатура действия с своей анкетой, при отсуствии её'''
    buttons = [
        [KeyboardButton(text=msg_text.create_master_profile)],
        back_to_menu
    ]
    kb = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return kb

def get_back_keyboard() -> ReplyKeyboardMarkup:
    buttons = back_to_menu
    kb = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return kb

def get_after_rewrite_profile_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text=msg_text.published)],
        back_to_menu
    ]
    kb = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return kb