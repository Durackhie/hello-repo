import os
from telegram import Bot
import asyncio

# Токен вашего бота, полученный от BotFather
bot_token = "YOUR_BOT_TOKEN"

# Айди чата, куда вы хотите отправить уведомления
chat_id = "YOUR_CHAT_ID"

# Инициализация бота
bot = Bot(token=bot_token)

async def send_telegram_message(text):
    await bot.send_message(chat_id=chat_id, text=text)

if __name__ == "__main__":
    # Ваш код или запуск тестов

    # Если произошла ошибка
    error_occurred = True

    if error_occurred:
        error_message = "Произошла ошибка с кодом 1"
        loop = asyncio.get_event_loop()
        loop.run_until_complete(send_telegram_message(error_message))
