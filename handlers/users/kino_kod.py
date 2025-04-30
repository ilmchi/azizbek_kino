from idlelib.window import add_windows_to_menu
from importlib.metadata import files
from tkinter.tix import ASCII
from token import AWAIT

from states.kino import KinoState
from loader import dp,bot,kinodb
from aiogram import types
from aiogram.dispatcher import FSMContext
from data .config import ADMINS



@dp.message_handler(commands="kino_add")
async def kino_add_function(message:types.Message):
    await message.answer("kinoni yubor")
    await KinoState.kino.set()


@dp.message_handler(state=KinoState.kino,content_types=types.ContentType.VIDEO)
async def kino_add_content(message:types.Message,state:FSMContext):
    async with state.proxy () as data:
        data ['file_id']=message.video.file_id
        data['caption']=message.caption or 'Kino'
    await message.answer('kino uchun kod kirit')
    await KinoState.kod.set()
@dp.message_handler(state=KinoState.kod,content_types=types.ContentType.TEXT)
async def kino_add_kod(message:types.Message,state:FSMContext):
     try:
         post_id=int (message.text)
         async with state .proxy() as data:
             data ['post_id']=post_id
             await kinodb.add_kino(post_id=data['post_id'],
                                   file_id=data['file_id'],
                                   caption=data['caption']
                                   )

         await message.answer("kino mufaqiyatli qushildi ")
         await state.finish()
     except ValueError:
         await message.answer("kino uchun kod kiriting")


@dp.message_handler(lambda message:message.text.isdigit())
async def kino_top(message:types.Message):
    post_id=int(message.text)
    data=await kinodb.get_kino_by_post_id(post_id=post_id)
    if data :
        try:
            kinodb.increment_kino_views(post_id=post_id)
            await bot.send_video(chat_id=message.from_user.id,
                                 video=data['file_id'],
                                  caption=f"{data['caption']}\n\n@judochi_bot")
        except:
               await message.answer("kino topildi yuborishda xatolik")
        else:
               await message.answer("kino topilmadi")
    else:
         await message.answer("kino uchun kod raqam sifatida kirting ")








