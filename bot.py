import asyncio

from aiogram import types
from aiogram.dispatcher import router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from create_bot import dp, bot

import keyboard
import function as f

class Form(StatesGroup):
    to_fix = State()
    to_upgrade = State()

@dp.message(Command('start'))
async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                           "👋 Welcome to GrammarlyBot! \n"
                           "I'm here to help you improve your writing and make it flawless. Whether you're working on an important email, an essay, or just want to enhance your communication skills, I've got you covered.\n"
                           "Here's how I can assist you:\n"
                           "✍️ **Grammar Check**: Send me your text, and I'll review it for grammatical errors and suggest corrections.\n"
                           "📝 **Spelling Check**: Worried about typos? I'll catch those too!\n"
                           "🔍 **Vocabulary Enhancement**: Need to elevate your language? I can suggest better word choices.\n"
                           "📖 **Style Improvements**: I'll help you polish your writing style for clarity and coherence.\n"
                           "If you ever need assistance or have questions, feel free to type \"/help\" anytime.\n"
                           "Let's make your writing shine! ✨\n")


@dp.message(Command('menu'))
async def choose_opt(message: types.Message):
    await bot.send_message(message.chat.id, 'Choose your option:', reply_markup=keyboard.menu)


@dp.callback_query()
async def functionality(call: CallbackQuery, state: FSMContext):
    if call.data == 'fix':
        await bot.send_message(call.from_user.id, 'Write down your text to fix')
        await state.set_state(Form.to_fix)


@dp.message(Form.to_fix)
async def return_fix(message: types.Message, state: FSMContext):
    mess = await f.str_to_list(message.text)
    await bot.send_message(message.chat.id, str(mess) + '\n\nstop')
    await state.clear()


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
