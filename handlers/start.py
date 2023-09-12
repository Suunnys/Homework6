from aiogram import types,Dispatcher
from config import bot
from const import START_TEXT
from database.sql_commands import Database
from keybords.inline_buttons import start_keyboard


async def start_button(message:types.Message):

    Database().sql_insert_user_command(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )

    print(message)
    await bot.send_message(
        chat_id=message.chat.id,
        text=START_TEXT.format(
            username=message.from_user.username
        ),
        parse_mode=types.ParseMode.MARKDOWN,
        reply_markup= await start_keyboard()

    )




def register_start_hendlers(dp:Dispatcher):
    dp.register_message_handler(start_button,commands=["start"])