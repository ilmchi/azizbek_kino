from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.postreskl import Database
from data import config
from utils.db_api.postreskl import Database
from utils.db_api.users import UserDatabase
from utils.db_api.kinodb import KinoDatabase
from data import config


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db=Database()
userdb=UserDatabase()
kinodb=KinoDatabase()
