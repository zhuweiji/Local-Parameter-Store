"""responds to a start command sent by the user 
i.e. /start

provides information about the functions the bot provides"""

import io
import logging
from datetime import datetime, timedelta
from uuid import uuid4

from telegram import Update
from telegram.ext import ContextTypes

log = logging.getLogger(__name__)

async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message: return

    await update.message.reply_text(
        text="""
Received your rejection!
        """
    )