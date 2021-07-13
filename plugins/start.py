from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start414"]), group=-2)
async def start414(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔥Channel🔥", url="https://t.me/joinchat/dK29OVb4ktxkODhl")],
        [InlineKeyboardButton(
            "💢Contact Admin💢", url="https://t.me/@RedX14")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
