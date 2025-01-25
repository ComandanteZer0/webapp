from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp,bot
from markups.inline.main_markups_inline import startWebApp
from data import config
@dp.message_handler(CommandStart(),state= '*')
async def bot_start(message: types.Message):
    if message.chat.type == 'private':
        
        await bot.delete_message(message.chat.id, message.message_id) 

        await bot.send_message(message.from_user.id, 
            f'startovoe mesage', 
        reply_markup=startWebApp())
            
'''@dp.callback_query_handler( text = "принять_правила",state= '*')
async def print_pravila(call: types.CallbackQuery):	
    await call.message.delete()
    await bot.send_message(call.message.chat.id, 
        f"❤️ {call.from_user.first_name}, приветствуем тебя в X-store LOGS SHOP \n"
        f"📚 Прочитай правила \n"
        f"📙 <a href='https://zelenka.guru/threads/4936053/'>Будем рады вашему отзыву </a>\n\n", 
        reply_markup=main_menu())

    await call.answer()'''