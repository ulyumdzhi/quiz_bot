import os
from aiogram import Bot, Dispatcher

TOKEN = os.environ['TOKEN']

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)