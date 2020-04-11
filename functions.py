import logging
import handlers
import commands
import jobs
import requests
from telegram.ext import MessageHandler, CommandHandler, CallbackContext

def logs():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

def check_connection(host):
    logging.info("Testing connection to %s" % (host))
    try:
        response = requests.get(host, timeout=10)
        if (response.status_code == 200):
            status = True
        time = response.elapsed.total_seconds()
    except OSError:
        status = False
        time = None
    return (status, time)

def sendStatusMsg(bot, update, msg):
    bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=msg)

def handlersProcess(updater, dispatcher):
    # Command handlers
    command_dict = dict(multimedia=CommandHandler('multimedia', commands.multimedia),
                        onepiece=CommandHandler('onepiece', commands.onepiece),
                        doctorwho=CommandHandler('doctorwho', commands.doctorwho))
    for command in command_dict:
        dispatcher.add_handler(command_dict[command])

    # Error handler
    dispatcher.add_error_handler(handlers.error)

    # Forward admin message handler
    dispatcher.add_handler(MessageHandler(None, handlers.adminForward))

    # Start the bot
    updater.start_polling()

    # Wait for Ctrl-C or other SIGs to end the process
    updater.idle()

def handleJobs(jobqueue, dispatcher):
    dispatcher.bot_data["top"] = ""
    job_multimediaQueue = jobqueue.run_repeating(jobs.multimediaQueue, interval=5, first=0)
