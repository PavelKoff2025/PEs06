import os
import logging
from dotenv import load_dotenv
from openai import OpenAI
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

# --- Загрузка переменных окружения ---
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ASSISTANT_ID = os.getenv('ASSISTANT_ID')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# --- Проверка переменных ---
if not all([OPENAI_API_KEY, ASSISTANT_ID, TELEGRAM_TOKEN]):
    raise ValueError("Не все обязательные переменные окружения установлены!")

# --- Инициализация клиентов ---
client = OpenAI(api_key=OPENAI_API_KEY)

# --- Логирование ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
user_threads = {}


# --- Приветственное сообщение ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я бот-помошник.\n"
        "Отправь любое сообщение, и я передам его ассистенту OpenAI."
    )


# --- Основная логика ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user_id = update.message.from_user.id

    status_msg = await update.message.reply_text("Обрабатываю запрос...")

    try:
        # Создание или получение треда пользователя
        if user_id in user_threads:
            thread_id = user_threads[user_id]
        else:
            thread = client.beta.threads.create()
            thread_id = thread.id
            user_threads[user_id] = thread_id

        # Отправка сообщения в тред
        client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_message
        )

        # Запуск ассистента
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=ASSISTANT_ID
        )

        # Ожидание завершения
        while run.status in ("queued", "in_progress"):
            run = client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id
            )

        # Получение ответа
        messages = client.beta.threads.messages.list(thread_id=thread_id)

        response_texts = [
            msg.content[0].text.value
            for msg in reversed(messages.data)
            if msg.role == "assistant"
        ]

        response = "\n".join(response_texts) if response_texts else "Нет ответа от ассистента."
        await status_msg.edit_text(response)

    except Exception as e:
        logger.error(f"Ошибка: {e}")
        await status_msg.edit_text("Ошибка при обработке запроса. Попробуйте позже.")


# --- Запуск бота ---
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("✅ Бот запущен!")
    app.run_polling()


if __name__ == "__main__":
    main()