import asyncio

from aiogram import types
from aiogram.filters.command import Command


from create_bot import dp, bot


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
                           "To get started, simply send me your text, and I'll do the rest. You can also use commands to specify the type of check you need. For example, send \"/grammar\" for a grammar check or \"/spelling\" for a spelling check.\n"
                           "If you ever need assistance or have questions, feel free to type \"/help\" anytime.\n"
                           "Let's make your writing shine! ✨\n")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
