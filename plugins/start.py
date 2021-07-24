from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔰Update Channel🔰", url="https://t.me/redx414news")],
        [InlineKeyboardButton("♨️Contact Admin♨️", url="https://t.me/RedX14")]
    ])
    welcomed = f"<b>Hello {message.from_user.first_name}</b>\n\nYou Can Download Youtube Videos Using Me😋\n\nClick the /help Button to Find Out How to Use Me🤪"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
