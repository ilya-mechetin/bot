import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup
bot =Bot(token = '1873084290:AAHbcKsQqmII3HZEyGXRo3f16WBvRQw2P0U')
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет", reply_markup=greet_kb)
button_hi = KeyboardButton('Привет')
greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)
button_bye = KeyboardButton('Пока')
greet_kb.add(button_kb)
if __name__ == '__main__':
    executor.start_polling(dp)
