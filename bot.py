import telebot
import subprocess
import time
import pyperclip

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

ADMIN_ID =
def notify_admin(message, prefix="📩"):
    """Отправка сообщения админу (текст команды или обычное сообщение)"""
    if message.from_user.id != ADMIN_ID:
        try:
            bot.send_message(
                ADMIN_ID,
                f"{prefix} От @{message.from_user.username or 'без username'} (ID: {message.from_user.id}):\n\n{message.text}"
            )
        except Exception as e:
            print(f"Ошибка при отправке админу: {e}")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет, это бот для быстрого взаимодейсвтия с VPn")
    notify_admin(message, "🟢 Команда /start")

@bot.message_handler(commands=['info'])
def info_message(message):
    bot.send_message(message.chat.id, 'Это крутой впн')
    notify_admin(message, "🟢 Команда /info")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Напиши старт /start')
    notify_admin(message, "🟢 Команда /help")

@bot.message_handler(commands=['send'])
def send_message(message):
    bot.send_message(message.chat.id, 'всязтяться с ukfdysv - ')
    notify_admin(message, "🟢 Команда /send")

ADMIN_ID =
COOLDOWN_SECONDS = 1  # время между вызовами для каждого пользователя
user_last_command_time = {}  # словарь: user_id -> время последнего вызова
FILE_PATH = 'saved_text.txt'  # файл для сохранения текста из буфера
@bot.message_handler(commands=['path'])
def path_message(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Проверка на доступ
    if user_id != ADMIN_ID:
        bot.send_message(chat_id, "⛔ Команда недоступна.")
        return

    # Получаем время последнего вызова (по умолчанию 0)
    last_time = user_last_command_time.get(user_id, 0)
    current_time = time.time()

    if current_time - last_time < COOLDOWN_SECONDS:
        remaining = int(COOLDOWN_SECONDS - (current_time - last_time))
        bot.send_message(chat_id, f"⏳ Подождите {remaining} сек. перед следующим запуском.")
        return

    try:
        subprocess.Popen(["python", "start-amnezia.py"])
        bot.send_message(chat_id, "✅ AmneziaVPN запускается...")
        user_last_command_time[user_id] = current_time  # обновляем таймер для пользователя

        # Ждём, чтобы буфер обмена обновился после клика "Скопировать"
        time.sleep(22)

        clipboard_text = pyperclip.paste()
        if clipboard_text:
            # Сохраняем текст из буфера в файл
            with open(FILE_PATH, 'w', encoding='utf-8') as f:
                f.write(clipboard_text)

        # Чтение из буфера обмена
        clipboard_text = pyperclip.paste()
        if clipboard_text:
            bot.send_message(chat_id, f"📋 Содержимое буфера обмена:\n{clipboard_text}")
        else:
            bot.send_message(chat_id, "❌ Буфер обмена пуст.")

    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка запуска: {e}")

# Новый обработчик для команды /find
@bot.message_handler(commands=['find'])
def find_command(message):
    chat_id = message.chat.id
    try:
        with open(FILE_PATH, 'rb') as f:
            bot.send_document(chat_id, f)
    except FileNotFoundError:
        bot.send_message(chat_id, "Файл с текстом пока не создан. Вызовите /path для создания.")

# 🆕 Обработчик всех прочих сообщений — пересылает их админу
@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    if message.from_user.id != ADMIN_ID:
        try:
            bot.send_message(
                ADMIN_ID,
                f"📩 Новое сообщение от @{message.from_user.username or 'без username'} "
                f"(ID: {message.from_user.id}):\n\n{message.text}"
            )
        except Exception as e:
            print(f"Ошибка при отправке сообщения админу: {e}")

bot.infinity_polling()