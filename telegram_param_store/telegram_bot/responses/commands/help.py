"""responds to a start command sent by the user 
i.e. /start

provides information about the functions the bot provides"""

import io
import logging
from datetime import datetime, timedelta
from uuid import uuid4

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

log = logging.getLogger(__name__)

async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message: return

    await update.message.reply_text(
        text="""
Hello!
        
This is the companion Telegram bot for the Parameter Store service.
        """
    )