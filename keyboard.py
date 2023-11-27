from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Correct',
            callback_data='fix'
        )
    ],
    [
        InlineKeyboardButton(
            text='Upgrade',
            callback_data='upgrade'
        )
    ],
    [
        InlineKeyboardButton(
            text='Paraphrase',
            callback_data='paraphrase'
        )
    ]
])
