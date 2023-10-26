import telegram
from telegram.ext import Updater, CommandHandler

# Замените <YOUR_BOT_TOKEN> на токен вашего бота
bot_token = "6693782514:AAGheL0DF6SNZXQGsks_2I80vlLvz9StyEA"

# Замените <YOUR_CHAT_ID> на ID вашего чата
chat_id = "-1001988273555"

bot = telegram.Bot(token=bot_token)
await bot.send_message(chat_id=chat_id, text="Тесты завершились неудачей.")
