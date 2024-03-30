from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def button(url, availability_0_0):
    return InlineKeyboardMarkup().row(
        InlineKeyboardButton('◀', callback_data='back'),
        InlineKeyboardButton(availability_0_0, callback_data='AVAILABILITY'),
        InlineKeyboardButton('▶', callback_data='NEXT')
    ).row(
        InlineKeyboardButton('Reference', url=url)
    )