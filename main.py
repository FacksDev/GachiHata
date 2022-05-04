#!/bin/python3
import logging
from datetime import datetime

from gino import Gino
from aiogram import Bot, Dispatcher, executor, types
import aioschedule
import asyncio

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP

import database
import distributor

API_TOKEN = '5343445681:AAGJVCks7Gx58Q9ShrPEPrssZh4yylEi2ME'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Gino()


class User(db.Model):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    name = Column(String(32))


class TaskType(db.Model):
    __tablename__ = "task_types"
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    value = Column(Integer)
    repeat_days = Column(Integer)


class Task(db.Model):
    __tablename__ = "task_types"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    task_type_id = Column(Integer, ForeignKey("task_types.id"))
    added_at = Column(TIMESTAMP(), default=datetime.utcnow, nullable=True)
    competed_at = Column(TIMESTAMP(), default=datetime.utcnow, nullable=True)
    deadline = Column(TIMESTAMP(), default=datetime.utcnow, nullable=True)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def assign_required_tasks():
    # collect_tasks()...
    # distribute_tasks()...
    pass


async def scheduler():
    aioschedule.every().day.do(assign_required_tasks)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(228)


async def main(*args):
    await db.set_bind('postgresql://localhost/gino')
    await db.gino.create_all()
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=main)
