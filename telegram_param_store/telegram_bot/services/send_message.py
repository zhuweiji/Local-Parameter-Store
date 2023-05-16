import io
import logging
from datetime import datetime, timedelta
from uuid import uuid4

import httpx
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineQueryResultDocument,
    InputFile,
    InputMediaDocument,
    InputTextMessageContent,
    Update,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    InlineQueryHandler,
    MessageHandler,
    Updater,
    filters,
)

from telegram_param_store.parameter_manager.parameter_manager import ParameterManager
from telegram_param_store.telegram_bot.main import TOKEN

log = logging.getLogger(__name__)

def send_message_to_defined_user(message:str):
    chat_id = 407132829
    
    log.info('attempting to send message to user')
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}'

    response = httpx.get(url)
    if not response.status_code == 200:
        log.exception(response)
    return response.status_code == 200



