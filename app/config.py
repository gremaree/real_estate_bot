from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()
        self.bot_token = os.getenv("BOT_TOKEN")
        self.db_url = os.getenv("DATABASE_URL")

def load_config(path: str = ".env") -> Config:
    return Config()
