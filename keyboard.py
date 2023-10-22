from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Correct the text',
            callback_data='fix'
        )
    ],
    [
        InlineKeyboardButton(
            text='Upgrade the text',
            callback_data='upgrade'
        )
    ]
])
