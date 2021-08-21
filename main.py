# pip install -U aiogram
# pip install qrcode[pil]

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
import json

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


async def create_qr(bot, message):
    # TODO: Реализовать отправку str_code в базу данных
    print(type(str(message.from_user.id)))
    str_code = str(ran(100, 999)) + str(message.from_user.id) + str(ran(100, 999))
    print(str_code)  # Уникальный код для пользователя
    qr.add_data(str_code)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    name_file = str_code + ".png"  # Имя файла
    print("Name file =", name_file)
    path_img = "QR_img\\" + name_file  # Полный путь к картинки
    img.save(path_img)

    print("QR code created")

    await bot.send_message(message.from_user.id, 'Ваш QR-код на скидку')
    with open(path_img, 'rb') as photo:
        await bot.send_photo(
            message.from_user.id, photo
        )
    await bot.send_message(message.from_user.id, 'Покажи его администратору на стойке в начале посещения, чтобы '
                                                 'активировать скидку.')

    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), path_img)
    os.remove(path)
    print('Image has been deleted')


async def read_and_write_json(id_user, str_code):
    # Открываем data_base.json
    with open('data_base.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        data[str(id_user)] = str_code

    with open('data_base.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))
    print(data)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет!\n Напиши мне что-нибудь.")
    # await message.reply("Привет\nНапиши мне что-нибудь!") \
    # reply - отправляет сообщение пользователя с пересылкой сообщения
    # send_message - отправка обычного сообщения


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Напиши мне что-нибудь")


@dp.message_handler(commands=['json'])
async def process_help_command(message: types.Message):
    await read_and_write_json(message.from_user.id + 2, '34234dsd')


@dp.message_handler(commands=['qr'])
async def process_help_command(message: types.Message):
    # await bot.send_message(message.from_user.id, "Здесь будет реализована функция, которая будет создавать qr код")
    await create_qr(bot, message)


@dp.message_handler()  # Пустые скобки = обработка текста
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    # send_message - отправка обычного сообщения


if __name__ == '__main__':
    executor.start_polling(dp)
