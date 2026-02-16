# Импортируем нужные инструменты из библиотеки
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Команда /start — приветствие
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я Эхо, твой бот 🤖")

# Команда /help — список возможностей
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я умею:\n"
        "/start - приветствие\n"
        "/help - показать список команд\n"
        "А ещё я повторяю твои сообщения!"
    )

# Эхо — повторяет любое сообщение
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def main():
    # Соединяем код с ботом благодаря токену
    app = ApplicationBuilder().token("Твой токен").build()

    # Добавляем команды и обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    app.run_polling()

# Запуск программы
if __name__ == "__main__":
    main()