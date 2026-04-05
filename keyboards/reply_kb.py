from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_to_menu =[KeyboardButton(text="Вернуться в главное меню")]

def get_main_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Найти мастера")],
        [KeyboardButton(text="Создать анкету мастера")],
        [KeyboardButton(text="Моя анкета")]
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
        [KeyboardButton(text="Создать анкету мастера")],
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
        [KeyboardButton(text="Опубликовать")],
        [KeyboardButton(text="Оставить не опубликованной")],
        back_to_menu
    ]
    kb = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return kb