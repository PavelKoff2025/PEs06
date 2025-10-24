import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Получаем токен
token = os.getenv('TELEGRAM_BOT_TOKEN')
print(f"Token: {token}")

# Ваш основной код здесь
print("Программа работает!")
