from aiogram import Bot, types

kino_id_lugat = {
    "1234": 4,
    "5678": 5
}

async def send_movie(bot: Bot, message: types.Message, channel_id: str):
    kino_id = message.text.strip()
    if kino_id.isdigit() and kino_id in kino_id_lugat:
        xabar_id = kino_id_lugat[kino_id]
        await bot.copy_message(chat_id=message.chat.id, from_chat_id=channel_id, message_id=xabar_id)
    else:
        await message.reply("❌ Bunday kino topilmadi. Iltimos, boshqa kod kiriting!")
