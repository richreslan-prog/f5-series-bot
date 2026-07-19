import os
from pyrogram import Client, filters

app = Client(
    "F5_SERIES",
    api_id=int(os.environ["23948220"]),
    api_hash=os.environ["b8680feab0feb7061f07479f62f10049"],
    bot_token=os.environ["8801205172:AAEMnpqnqfcB9NZeUMXsmQtGxkkA6MsEhCY"]
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply(
        "🎬 Welcome to F5 SERIES!\n\nSend me a movie name."
    )

app.run()
