from decouple import config
from aiogram import Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot= bot, storage=storage)
ADMIN_ID = 5231320095
BOT_PIC = '/home/umar/PycharmProjects/pythonProject/media/bot_pic.jpg'
ANIMATION_PIC = "/home/umar/PycharmProjects/pythonProject/media/df1ilux-62c4303b-7ff2-4e4a-b429-6598d6cc656c.gif"
GROUP_ID = -4012849376
DESTINATION_DIR = None