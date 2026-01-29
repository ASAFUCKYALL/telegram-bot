from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes
import os

TOKEN = os.environ.get("BOT_TOKEN")

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()

app = Application.builder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(approve))

print("Bot actif (GitHub Actions)")
app.run_polling()
