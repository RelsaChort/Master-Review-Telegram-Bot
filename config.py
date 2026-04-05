import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEB is not set")

DB_URL = os.getenv("DB_URL")
if not DB_URL:
    raise ValueError("DataBase URL is not set")

ADMIN_ID = [int(id_str) for id_str in os.getenv("ADMIN_ID", "").split(",") if id_str]
