
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup

from aiogram import types



def main_menu():
    webAppInfo = types.WebAppInfo(url="your-webapp-url")
    web_app=webAppInfo
    main_menu = ReplyKeyboardMarkup(resize_keyboard=True).row(
        'Открыть магазин',web_app=webAppInfo)
    return main_menu
