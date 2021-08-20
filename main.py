# pip install -U aiogram
# pip install qrcode[pil]

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

import qrcode

import os

from random import randint as ran

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=100,
    border=4,
)

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


@dp.message_handler(commands=['qr'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Здесь будет реализована функция, которая будет создавать qr код")
    print(type(str(message.from_user.id)))
    str_code = str(ran(100, 999)) + str(message.from_user.id) + str(ran(100, 999))
    print(str_code)
    qr.add_data(str_code)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    name_file = str_code + ".png"
    print("Name file =", name_file)
    img.save("QR_img\\" + name_file)

    print("QR code created")

    # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "QR_img\\" + name_file)
    # os.remove(path)
    # print('Image has been deleted')


@dp.message_handler()  # Пустые скобки = обработка текста
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    # send_message - отправка обычного сообщения


if __name__ == '__main__':
    executor.start_polling(dp)
