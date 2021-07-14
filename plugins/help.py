from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help414"]))
async def start(client, message):
    helptxt = f"🚫You Can't Download YT Playlists From Our Bot🚫

🔥Just Download One Video at a Time🔥"
    await message.reply_text(helptxt)
