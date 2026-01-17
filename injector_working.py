import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Включим логирование, чтобы видеть ошибки
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        f"Привет, {user.mention_html()}! Я бот. Как дела?",
    )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Помощь! Я пока понимаю только команды /start и /help.")

def main():
    # Создаем Application и передаем ему токен вашего бота.
    application = Application.builder().token('8307220224:AAGWDTLTckiMy3_kApiPHJJnEOTmJliwzDg').build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Запускаем бота до остановки пользователем (Ctrl+C)
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()