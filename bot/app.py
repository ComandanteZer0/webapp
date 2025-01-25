

from loader import dp
import os
from aiogram import executor
import asyncio
import  handlers
if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    executor.start_polling(dp)

    

