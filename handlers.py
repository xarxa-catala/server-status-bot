import functions
import logging
import sys

try:
    from settings_secret import *
except:
    sys.exit("Missing settings_secret.py file.")

def error(update, context):
    logger = functions.logs()
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def adminForward(update, context):
    if (update.message.chat_id in admins_id.values()):
        for send_id in notify_dest_id.values():
            context.bot.send_message(chat_id=send_id, text=update.message.text)
            logging.info("Message from %d forwarded to %d." % (update.message.chat_id, send_id))
