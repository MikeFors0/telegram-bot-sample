from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(msg:Message):
    await msg.answer("Запуск сообщения по команде /start используя фильтр CommandStart()")


@start_router.message(Command('start_2'))
async def cmd_start_2(msg: Message):
    await msg.answer("Запуск сообщения по команде /start_2 используя фильтр Command()")


@start_router.message(F.text == '/start_3')
async def cmd_start_3(msg: Message):
    await msg.answer("Запуск сообщения по команде /start_3 используя магический фильтр F.text!")