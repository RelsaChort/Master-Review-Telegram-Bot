import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEB is not set")

ADMIN_ID = [int(id_str) for id_str in os.getenv("ADMIN_ID", "").split(",") if id_str]
