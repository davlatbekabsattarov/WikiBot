import types
import wikipedia
import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import types


TOKEN = "6929944222:AAEOpQePZKIHGWhAEwRhKs_H7KiE4Te_CbQ"
wikipedia.set_lang('uz')
dp = Dispatcher()
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Assalamu aleykum, {html.bold(message.from_user.full_name)}!\n Qidirmoqchi bo'lgan ma'lumotingizni kiriting:")

@dp.message()
async def wiki_sender(message: types.Message):

    try:
        response=wikipedia.summary(message.text)
        await message.answer(response, "Yana nimani topay?")
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Yaxshi urunish!")
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi!!!")




async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
