from settings_secret import notify_dest_id
from emoji import emojize
import telegram.ext
import requests
import os

def multimediaQueue(context: telegram.ext.CallbackContext):
    top = context.bot_data["top"]
    r = requests.get(url='https://gestor.multimedia.xarxacatala.cat/cua/')
    queue = r.json()

    if not queue:
        if top != "":
            filename = os.path.basename(top[top.find("=")+2:-1])
            msg = emojize(filename + " :white_check_mark:", use_aliases=True)
            context.bot.send_message(chat_id=notify_dest_id["Xarxa Cat"], text=msg)
            context.bot_data["top"] = ""            
    elif queue[0] != top:
        if top != "":
            filename = os.path.basename(top[top.find("=")+2:-1])
            msg = emojize(filename + " :white_check_mark:", use_aliases=True)
            context.bot.send_message(chat_id=notify_dest_id["Xarxa Cat"], text=msg)
        context.bot_data["top"] = queue[0]
