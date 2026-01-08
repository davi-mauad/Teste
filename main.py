import os
from bot_multimodal import BotMultimodal

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = BotMultimodal(TOKEN)
bot.run()