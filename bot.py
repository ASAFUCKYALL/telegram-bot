from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes

TOKEN = "8507624503:AAGcpEuqwpSqNW7JJTdTKz8WCTWiiInAY-c"

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()

app = Application.builder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(approve))

print("Bot actif")
app.run_polling()