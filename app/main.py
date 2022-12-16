import os
import logging

from aiogram import executor
from handlers.dp import dp


logging.basicConfig(level=logging.INFO, 
                    filename='./log/log.log')


if __name__ == '__main__':
    # os.system('python db/init_base.py')
    executor.start_polling(dp, skip_updates=True)