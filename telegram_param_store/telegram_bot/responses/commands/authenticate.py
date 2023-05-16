"""responds to a start command sent by the user 
i.e. /start

provides information about the functions the bot provides"""

import io
import logging
from datetime import datetime, timedelta
from uuid import uuid4

from telegram import Update
from telegram.ext import ContextTypes

from telegram_param_store.parameter_manager.parameter_manager import ParamRequestManager

log = logging.getLogger(__name__)

async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message: return
    
    auth_request_id = update.message.text
    
    if not auth_request_id: 
        log.warning('received authentication command but no request_id received')
        return
    
    await update.message.reply_text(
        text="""
Received your authentication!
        """
    )
    # todo this should be tied to how the command is declared in main.py
    auth_request_id = auth_request_id.replace('/authenticate','').replace('/auth','').strip()
    
    result = ParamRequestManager.complete_auth_request__id(auth_request_id)
    if result:
        await update.message.reply_text(text="Authentication completed successfully!")   
    else:
        await update.message.reply_text(text="Authentication was not completed successfully")   