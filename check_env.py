from dotenv import load_dotenv
import os

load_dotenv()

print("TELEGRAM_TOKEN:", "✅ Установлен" if os.getenv('TELEGRAM_TOKEN') else "❌ Отсутствует")
print("OPENAI_API_KEY:", "✅ Установлен" if os.getenv('OPENAI_API_KEY') else "❌ Отсутствует")
print("ASSISTANT_ID:", "✅ Установлен" if os.getenv('ASSISTANT_ID') else "❌ Отсутствует")
