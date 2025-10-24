# Telegram Bot Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-brightgreen.svg)](https://docs.aiogram.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Умный и многофункциональный бот-ассистент для Telegram, разработанный на Python.
Задача бота помочь преподавателям создавать структуру учебных материалов: пособий, лекций, уроков и т.д.

---

## 🚀 Функционал

*   **Приветствие:** Привет! Я бот-помошник.
Отправь любое сообщение, и я передам его ассистенту OpenAI.
*   **Ввод запроса пользователя:** Создай структуру учебного пособия "Основы интернет-маркетинга"
*   **Получение ответа** Структура учебного пособия «Основы Интернет-маркетинга»

## 🛠️ Технологии

*   **Язык:** Python 3.8+
*   **Фреймворк:** [aiogram](https://docs.aiogram.dev/) 3.x (асинхронный)
*   **HTTP-запросы:** [aiohttp](https://docs.aiohttp.org/)
*   **Парсинг данных:** [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) / API
*   **Виртуальное окружение:** `venv`

---

## 📦 Установка и запуск

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/your_username/telegram-bot-assistant.git
    cd telegram-bot-assistant
    ```

2.  **Создайте и активируйте виртуальное окружение:**
    ```bash
    python -m venv venv
    # Для Linux/macOS:
    source venv/bin/activate
    # Для Windows:
    .\venv\Scripts\activate
    ```

3.  **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Настройка конфигурации:**
    *   Создайте файл `.env` в корне проекта на основе примера `.env.example`.
    *   Получите токен бота у [BotFather](https://t.me/BotFather) и запишите его в `.env`:
        ```ini
        BOT_TOKEN=your_bot_token_here
        OPENAI_API_KEY=your_OPENAI_API_KEY_here
        ```

5.  **Запустите бота:**
    ```bash
    python bot.py
    ```

---

## 🗂️ Структура проекта
telegram-bot-assistant/
├── bot.py # Главный файл для запуска бота
├── handlers/ # Директория с обработчиками сообщений
│ ├── init.py
│ ├── start.py
├── services/ # Логика работы с внешними API
│ ├── init.py
├── .env.example # Пример файла с переменными окружения
├── requirements.txt # Список зависимостей
├── README.md # Документация проекта (этот файл)
└── .gitignore # Файлы, игнорируемые Git

---

## 👨‍💻 Разработчик

Павел Кариков – pavelkoff@gmail.com

*   GitHub: PavelKoff2025 (https://github.com/PavelKoff2025)
*   Telegram: @pavelkarikoff(https://t.me/PEs06_bot)

---
## 📄 Лицензия

Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для получения дополнительной информации.
