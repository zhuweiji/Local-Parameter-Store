import asyncio
import logging

from telegram_param_store.parameter_manager.parameter_manager import ParameterManager
from telegram_param_store.telegram_bot.main import telegram_bot_server
from telegram_param_store.webserver.main import webserver

logging.basicConfig(format='%(name)s-%(levelname)s|%(lineno)d:  %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)


async def main():
    manager = ParameterManager
    
    # https://github.com/python-telegram-bot/python-telegram-bot/wiki/Frequently-requested-design-patterns#running-ptb-alongside-other-asyncio-frameworks
    await telegram_bot_server.initialize()
    await telegram_bot_server.start()
    if not telegram_bot_server.updater: raise ValueError
    await telegram_bot_server.updater.start_polling()
    
    # Start other asyncio frameworks here
    await webserver.serve()
    # Add some logic that keeps the event loop running until you want to shutdown
    # Stop the other asyncio frameworks here
    
    await telegram_bot_server.updater.stop()
    await telegram_bot_server.stop()
    await telegram_bot_server.shutdown()
    
    
    
if __name__ == "__main__":
    asyncio.run(main())