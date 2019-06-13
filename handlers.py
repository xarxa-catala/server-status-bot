import functions
import logging
try:
    from settings_secret import *
except:
    sys.exit("Missing settings_secret.py file.")

def error(update, error):
    logger = functions.logs()
    logger.warning('Update "%s" caused error "%s"', update, error)

def adminForward(bot, update):
    if (update.message.chat_id in admins_id ):
        bot.send_message(chat_id=notify_dest_id, text=update.message.text)
        logging.info("Message from %d forwarded to %d." % (update.message.chat_id, notify_dest_id))
