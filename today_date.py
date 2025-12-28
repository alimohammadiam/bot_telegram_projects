from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
import time


load_dotenv()

API_KEY = os.getenv('BOT_TOKEN')


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('جونم !!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('help_command!!')


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = str(update.message.text).lower()
    if text in ('تاریخ', 'چندمه', 'امروز'):
        result = time.time()
    else:
        result = 'I dont understand...!'

    await update.message.reply_text(result)


def main():
    application = Application.builder().token(API_KEY).build()

    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(MessageHandler(filters.TEXT, message_handler))

    print('robot is start to working...!')
    application.run_polling()


if __name__ == '__main__':
    main()