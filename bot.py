from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import executor
import asyncio
#=======my==================================================
from sql import Database
import os
import config
bot = Bot(token=config.botToken, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database("bd.db")
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup, WebAppInfo,BotCommand
@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    if message.chat.type == 'private':
        await bot.delete_message(message.chat.id, message.message_id) 
        if not db.user_exists( message.from_user.id):
            db.add_user(message.from_user.id)
        ikb_donate = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Перейти в магазин', web_app=WebAppInfo(url=config.main_link))
                                    ]
                                ])
        await bot.send_message(message.from_user.id, 
            f'Привет! Я бот для продажи мерча кампуса НЕЙМАРКА. Здесь вы можете найти уникальные товары, связанные с нашим брендом, включая одежду, аксессуары и сувениры.\n'
            f'Запусти меня, чтобы увидеть весь ассортимент!',  
        reply_markup=ikb_donate)
async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
        ]
    )
async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    executor.start_polling(dp,on_startup=on_startup)