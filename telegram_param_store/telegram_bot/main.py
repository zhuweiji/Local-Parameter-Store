import logging
import os
from pathlib import Path

from dotenv import dotenv_values
from telegram import (
    InlineQueryResultArticle,
    InlineQueryResultDocument,
    InputFile,
    InputMediaDocument,
    InputTextMessageContent,
    Update,
)
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    InlineQueryHandler,
    MessageHandler,
    PicklePersistence,
    TypeHandler,
    Updater,
    filters,
)

log = logging.getLogger(__name__)

from telegram_param_store.parameter_manager.dao import DAO
from telegram_param_store.telegram_bot.responses.commands import (
    authenticate,
    get,
    help,
    reject,
)
from telegram_param_store.telegram_bot.responses.normal_messages import handle_message
from telegram_param_store.telegram_bot.services import middleware

env_vars = dotenv_values()
os.environ.update(env_vars)

TOKEN = env_vars.get('BOTTOKEN')

if not TOKEN: 
    raise ValueError

persistence = PicklePersistence(filepath=Path(__file__).parent / 'bot_data')
telegram_bot_server = ApplicationBuilder().token(TOKEN).persistence(persistence).build()


telegram_bot_server.add_handler(TypeHandler(Update, middleware.pre_middleware),-1)

telegram_bot_server.add_handlers(handlers=[
    CommandHandler('help', help.handle_command),
    CommandHandler('get', get.handle_command),
    CommandHandler('authenticate', authenticate.handle_command),
    CommandHandler('auth', authenticate.handle_command),
    CommandHandler('reject', reject.handle_command),
    
    
    MessageHandler(filters=filters.TEXT & (~filters.COMMAND), callback=handle_message.handle_message),
        
])

if __name__ == "__main__":
    telegram_bot_server.run_polling()

