#!/bin/python3
import logging

from gino import Gino
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5343445681:AAGJVCks7Gx58Q9ShrPEPrssZh4yylEi2ME'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Gino()


# def assign_task(task, user):
#     pass

# def make_weekly_tasks():
#     pass
#
# def schedule_tasks(tasks, users):
#     pass

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main(*args):
    await db.set_bind('postgresql://localhost/gino')
    await db.gino.create_all()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=main)
