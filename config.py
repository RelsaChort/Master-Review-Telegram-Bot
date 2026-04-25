import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set")

DB_URL = os.getenv("DB_URL")
if not DB_URL:
    raise ValueError("DB_URL is not set")

ADMIN_ID = [
    int(id_str.strip()) 
    for id_str in os.getenv("ADMIN_ID", "").split(",") 
    if id_str.strip()
]