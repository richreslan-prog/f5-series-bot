import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ["8801205172:AAEMnpqnqfcB9NZeUMXsmQtGxkkA6MsEhCY"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Welcome to F5 SERIES!\n\nSend me a movie name."
    )

app = Application.builder().token(8801205172:AAEMnpqnqfcB9NZeUMXsmQtGxkkA6MsEhCY).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
