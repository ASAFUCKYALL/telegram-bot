from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes
import os
import sys

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    print("ERREUR : BOT_TOKEN manquant")
    sys.exit(1)
