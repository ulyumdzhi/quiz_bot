import logging
from aiogram import types

from bot.dispatcher import bot, dp

from codewars.task import Task

from config.admins import admin_id_list  # works in container after docker-compose up --build

from handlers.start import users_id



@dp.message_handler(content_types=['text'])
async def admin_tasks(message: types.Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    task_url = message.text
    task = Task(task_url)
    
    flag = False

    if user_id in admin_id_list:
        logging.info(f'{user_name=} {user_id=} send {task}')
        
        if task.name:
            await bot.send_message(user_id, f'*{task}* added and resend to users!', 
                                   parse_mode='Markdown',
                                   disable_web_page_preview=True)
            if not flag:
                for uid in admin_id_list:
                    try:
                        users_id.pop(users_id.index(uid))
                        flag = True
                    except Exception as e:
                        print(e)

            
            for user in users_id:
                await bot.send_message(user, task_url, 
                                       parse_mode='Markdown',
                                       disable_web_page_preview=True)
        else:
            await bot.send_message(user_id, f'Task was not added! *Check your link!*', 
                                   parse_mode='Markdown',
                                   disable_web_page_preview=True)
            

    
    

@dp.message_handler(content_types=['photo'])
async def admin_tasks(message: types.Message):
    
    if message.media_group_id is None:
        ### Get user's variables
        user_name = message.from_user.first_name
        user_id = message.from_user.id
        message_id = message.message_id

        # Define input photo local path
        screenshot_name = 'data/screenshot_%s_%s.jpg' %(user_id, message_id)
        await message.photo[-1].download(screenshot_name) # extract photo for further procceses

    for admin in admin_id_list:
        await bot.send_photo(admin, 
                             photo=open(screenshot_name, 'rb')) 
        
        await bot.send_message(admin, f'*{user_name}* send answer!', 
                               parse_mode='Markdown',
                               disable_web_page_preview=True)
    