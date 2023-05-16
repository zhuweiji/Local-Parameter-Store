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

from telegram_param_store.parameter_manager.parameter_manager import ParameterManager

log = logging.getLogger(__name__)

async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message: return
    
    await update.message.reply_text(
        text=f"""
Here are the parameters in the store:
{ParameterManager.get_all()}
        """
    )
    return