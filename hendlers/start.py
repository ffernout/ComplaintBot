from aiogram import Router, types, F
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command("start"))
@start_router.message(Command("старт"))
async def start_command(message: types.Message):
    first_name = message.from_user.first_name
    await message.reply(f"Привет, {first_name}! Вас приветствует бот жалоб.")

