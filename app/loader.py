import os
import argparse
import logging

from static.texts import loader_ValueError_text as ve_text

logging.basicConfig(level=logging.INFO)

# set username of system
os_username = 'user'

try:
    os_username = os.environ['USER']
except Exception as e:
    print(e)


print(f'🫶  Hello, {os_username}!')

# find TOKEN for telegram api from @BotFather
try:
    TOKEN = os.environ['TOKEN']
    
    # if you got no env variable named TOKEN - you can set that one with arg --t
except Exception as e:
    logging.info('No such env variable named TOKEN')
    parser = argparse.ArgumentParser(description='Setup')
    parser.add_argument('--token', 
                        dest='token', 
                        action='store',
                        help='set your token from BotFather')
    
    args = parser.parse_args()
    
    TOKEN = args.token

# Setup requirements
if TOKEN: 
    print('💫 TOKEN is settled. Ready to upgrade and install requirements...')
    
    os.system('python -m pip install --upgrade pip')
    
    print('🚀', 'pip upgrade is done!')
    print('🤖', 'install dependencies...')
    
    os.system('pip install -r requirements.txt')
    
    print(' 🔥'*4, 'requirements setup is done!', '🔥 '*4)

else:
    raise ValueError(ve_text.format(os_username))

del os_username