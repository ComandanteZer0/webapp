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
@dp.message_handler(commands=['start','open'])
async def bot_start(message: types.Message):
    if message.chat.type == 'private':
        if db.checkRules(message.from_user.id):
            await bot.delete_message(message.chat.id, message.message_id) 
            if not db.user_exists( message.from_user.id):
                db.add_user(message.from_user.id)
            ikb_donate = InlineKeyboardMarkup(row_width=1,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Перейти в магазин', web_app=WebAppInfo(url=config.main_link))
                                        ]
                                    ])
            await bot.send_message(message.from_user.id, config.helloText,reply_markup=ikb_donate)
        else:
            confirm = InlineKeyboardMarkup(row_width=1,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Соглашаюсь', callback_data="✅ConfirmRules")
                                        ]
                                    ])
            await bot.send_message(message.from_user.id, 
                config.helloText,  
            reply_markup=confirm)
            
            pass
async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
        ]
    )
async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
@dp.callback_query_handler( text_contains = "✅ConfirmRules")
async def Status_change(call: types.CallbackQuery):
    db.set_rules(1,call.message.chat.id)	
    await call.answer()
    try:
        await call.message.delete()
    except:
        pass
    ikb_donate = InlineKeyboardMarkup(row_width=1,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Перейти в магазин', web_app=WebAppInfo(url=config.main_link))
                                        ]
                                    ])
    
    await bot.send_message(call.message.chat.id, config.helloText, 
                    reply_markup = ikb_donate)
if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    executor.start_polling(dp,on_startup=on_startup)