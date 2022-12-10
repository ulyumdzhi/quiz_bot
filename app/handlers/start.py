import asyncio
import logging
from aiogram import types

from bot.dispatcher import bot, dp
from static.texts import HELLO

users_id = []

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    global users_id
    
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'Start message from {user_name=}, {user_id=}')
    
    await message.reply(text)
    await asyncio.sleep(2)
    await bot.send_message(user_id, HELLO, 
                           parse_mode='Markdown',
                           disable_web_page_preview=True)
    
    
    users_id.append(user_id)
    