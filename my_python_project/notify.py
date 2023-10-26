import os
from telegram import Bot

# Токен вашего бота, полученный от BotFather
bot_token = "6693782514:AAGheL0DF6SNZXQGsks_2I80vlLvz9StyEA"

# Айди чата, куда вы хотите отправить уведомления
chat_id = "-1001988273555"

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
        # Отправка уведомления о ошибке
        send_telegram_message(error_message)
