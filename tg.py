import subprocess

from config import *
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from post import main
import logging
import traceback
from core import post
import asyncio,time

logging.basicConfig(level=logging.INFO)

if TOKEN_TG_BOT:
    bot = Bot(token=TOKEN_TG_BOT)
    dp = Dispatcher(bot)
    code = """
from config import *
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from post import main
import logging
import traceback
import asyncio
from core import post
bot = Bot(token=TOKEN_TG_BOT)
dp = Dispatcher(bot)

async def on_startup():
    while True:
        await bot.send_message(TG_ID, str(post.posts()))
        break;

if __name__ == '__main__':
     asyncio.run(on_startup())
    #executor.start(future=on_startup)
    """
else:
    code = """
from core import post
while True:
    print(post.posts())
    """

proc = subprocess.Popen(
    ['python3', '-c', code]
)

@dp.message_handler(commands=['start'])
async def process_help_command(message: types.Message):
    proc = subprocess.Popen(
        ['python3', '-c', code]
    )
    await bot.send_message(message.from_user.id, "Старт")

@dp.message_handler(commands=['stop'])
async def process_help_command(message: types.Message):
    proc.kill()
    await bot.send_message(message.from_user.id, "Стоп")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)