from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = ("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/9d32e98be2e25cd233aa5.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/16bf30bf68842ea735775.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/THE_ROYAL_CHATTING")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Feelings4s")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", None).split()))

FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
