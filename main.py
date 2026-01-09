import os
from bot_multimodal import BotMultimodal

TOKEN = os.getenv("8479058192:AAHqYwqvh5dqNmnhl9YToT9_rMZtfXrywKY")

bot = BotMultimodal(TOKEN)

bot.run()
