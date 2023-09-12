from aiogram import executor
from config import dp
from handlers import start,callback
from database import sql_commands




async def onstart_up(_):
    db = sql_commands.Database()
    db.sql_create_tables()





start.register_start_hendlers(dp=dp)
callback.register_callback_handlers(dp=dp)


if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=onstart_up
    )
