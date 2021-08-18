# pip install -U aiogram

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет!\n Напиши мне что-нибудь.")
    # await message.reply("Привет\nНапиши мне что-нибудь!") \
    # reply - отправляет сообщение пользователя с пересылкой сообщения
    # send_message - отправка обычного сообщения


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Напиши мне что-нибудь")


@dp.message_handler()  # Пустые скобки = обработка текста
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    # send_message - отправка обычного сообщения


if __name__ == '__main__':
    executor.start_polling(dp)
