import requests

# Замените 'YOUR_BOT_TOKEN' на ваш токен бота
bot_token = "6693782514:AAGheL0DF6SNZXQGsks_2I80vlLvz9StyEA"
# Замените 'YOUR_CHAT_ID' на chat_id вашего чата
chat_id = "-1001988273555"

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': message}
    response = requests.get(url, params=params)
    return response.json() 
