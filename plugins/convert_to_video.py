import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
from sample_config import Config 
from pyrogram import Client, filters
from translation1 import Translation
from Tools.Download import download

@Client.on_message(filters.command(["c2v"]))
async def video(bot, update):
  if update.from_user.id in Config.BANNED_USER:
      await c.send_message(chat_id=update.chat.id, text=Translation.BANNED_TEXT)
  if update.from_user.id not in Config.BANNED_USER:
    if update.reply_to_message is not None:
      await download(bot, update)
    else:
       await bot.send_message(chat_id=update.chat.id, text=Translation.REPLY_TEXT)

@Client.on_message(filters.command(["c2d"]))
async def file(bot, update):
  if update.from_user.id in Config.BANNED_USER:
      await c.send_message(chat_id=update.chat.id, text=Translation.BANNED_TEXT)
  if update.from_user.id not in Config.BANNED_USER:
    if update.reply_to_message is not None:
      await download(bot, update)
    else:
       await bot.send_message(chat_id=update.chat.id, text=Translation.REPLY_TEXT)
