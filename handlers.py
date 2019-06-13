import functions

def error(update, error):
    logger = functions.logs()
    logger.warning('Update "%s" caused error "%s"', update, error)

def adminForward(bot, update):
    admins_id = [8303639]
    notify_dest_id = 8303639
    if (update.message.chat_id in admins_id ):
        bot.send_message(chat_id=notify_dest_id, text=update.message)