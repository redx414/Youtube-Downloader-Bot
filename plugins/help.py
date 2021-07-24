from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"<b>🔻Follow the Following Steps🔻/n/n◆Send a Youtube Video Url Directly to the Bot😉/n/n◈Pick the Quality that You Require😇/n/n◆Choose Wether You Want the Video as a Video or as a Document🙂/n/n◈It Will Take Some Time to Upload Your Video😐/n/n◆Now You Have Your Video😊/n/n◈Enjoy🙊❤️</b>"
    await message.reply_text(helptxt)
