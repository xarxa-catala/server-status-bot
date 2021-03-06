import functions
import logging
from emoji import emojize

def multimedia(update, context):
    status, time = functions.check_connection("https://multimedia.xarxacatala.cat")
    if (status):
        time = str(round(time, 3)).replace(".", ",")
        msg = emojize("Estat del servidor multimèdia: :white_check_mark:\n"
                      "Temps de resposta: " + time + " s", use_aliases=True)
    else:
        msg = emojize("Estat del servidor multimèdia: :x:", use_aliases=True)
    functions.sendStatusMsg(context.bot, update, msg)
    logging.info("Multimedia status message sent to %d." % (update.message.chat_id))

def onepiece(update, context):
    status, time = functions.check_connection("https://onepiece.xarxacatala.cat")
    if (status):
        time = str(round(time, 3)).replace(".", ",")
        msg = emojize("Estat de la web de One Piece: :white_check_mark:\n"
                      "Temps de resposta: " + time + " s", use_aliases=True)
    else:
        msg = emojize("Estat de la web de One Piece: :x:", use_aliases=True)
    functions.sendStatusMsg(context.bot, update, msg)
    logging.info("One Piece web status message sent to %d." % (update.message.chat_id))

def doctorwho(update, context):
    status, time = functions.check_connection("https://doctorwho.xarxacatala.cat")
    if (status):
        time = str(round(time, 3)).replace(".", ",")
        msg = emojize("Estat de la web de Doctor Who: :white_check_mark:\n"
                      "Temps de resposta: " + time + " s", use_aliases=True)
    else:
        msg = emojize("Estat de la web de Doctor Who: :x:", use_aliases=True)
    functions.sendStatusMsg(context.bot, update, msg)
    logging.info("Doctor Who web status message sent to %d." % (update.message.chat_id))
