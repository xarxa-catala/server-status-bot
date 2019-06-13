import logging
import handlers
from telegram.ext import MessageHandler, CommandHandler

def logs():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

def handlersProcess(updater, dispatcher):
    # Error handler
    dispatcher.add_error_handler(handlers.error)

    # Entry and exit handler
    dispatcher.add_handler(MessageHandler(None, handlers.adminForward))

    # Start the bot
    updater.start_polling()

    # Wait for Ctrl-C or other SIGs to end the process
    updater.idle()