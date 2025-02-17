import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv("BOT_TOKEN")
DEV_SERVER_ID = os.getenv("DEV_SERVER_ID")