

from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
import asyncio
from aiogram import types
def startWebApp():
    webAppInfo = types.WebAppInfo(url='https://miniapp-goshasn.amvera.io/')
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text = 'Открыть магазин',web_app=webAppInfo)
    keyboard.add(button)
    return keyboard
