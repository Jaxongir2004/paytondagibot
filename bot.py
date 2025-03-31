import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

TOKEN = "7630943846:AAHSU1nfcYVftaTlxbADp2L__UGSii2M4lE"

# ✅ Obunani tekshirish uchun kanallar
SUBSCRIPTION_CHANNELS = [
    "@maajjbbuurriiy1",  # 1-kanal (obuna uchun)
    "@maajjbbuurriiyy2",  # 2-kanal (obuna uchun)
]

# ✅ Kinolarni olish uchun kanal
MOVIE_CHANNEL = "@allalaassa"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

# === Obunani tekshirish ===
async def check_subscription(user_id: int) -> bool:
    for channel in SUBSCRIPTION_CHANNELS:
        try:
            member = await bot.get_chat_member(channel, user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False
        except:
            return False
    return True

# === Kino kodlari bazasi ===
kino_id_lugat = {
    "1234": 4,  # "1234" kodi bo‘yicha @allalaassa kanalidagi 4-chi postdagi video olinadi
    "5678": 5   # "5678" kodi bo‘yicha @allalaassa kanalidagi 5-chi postdagi video olinadi
}

# === Kino yuborish funksiyasi ===
async def send_movie(message: Message):
    kino_id = message.text.strip()
    if kino_id in kino_id_lugat:
        xabar_id = kino_id_lugat[kino_id]
        await bot.copy_message(chat_id=message.chat.id, from_chat_id=MOVIE_CHANNEL, message_id=xabar_id)
    else:
        await message.reply("❌ Bunday kino topilmadi. Iltimos, boshqa kod kiriting!")

# === /start komandasi ===
@dp.message(Command("start"))
async def start_command(message: Message):
    user_id = message.from_user.id

    if await check_subscription(user_id):
        await message.answer("✅ Siz barcha kanallarga qo‘shildingiz! Endi kino kodini kiriting 😊:")
    else:
        buttons = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📢 Kanal 1", url="https://t.me/maajjbbuurriiy1")],
            [InlineKeyboardButton(text="📢 Kanal 2", url="https://t.me/maajjbbuurriiyy2")],
            [InlineKeyboardButton(text="✅ Tekshirish", callback_data="check")]
        ])
        await message.answer(
            "❌ Iltimos, barcha kanallarga obuna bo‘ling va '✅ Tekshirish' tugmasini bosing.",
            reply_markup=buttons
        )

# === "Tekshirish" tugmasi bosilganda ===
@dp.callback_query(lambda c: c.data == "check")
async def check_subscription_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id

    if await check_subscription(user_id):
        await callback_query.message.edit_text("✅ Tabriklayman! Endi kino kodini kiriting 😊:")
    else:
        await callback_query.answer("❌ Siz hali barcha kanallarga obuna bo‘lmadingiz!", show_alert=True)

# === Kino kodi qabul qilish ===
@dp.message()
async def handle_movie_request(message: Message):
    user_id = message.from_user.id

    if await check_subscription(user_id):
        await send_movie(message)
    else:
        await message.answer("❌ Iltimos, barcha kanallarga obuna bo‘ling!")

# === Botni ishga tushirish ===
async def main():
    print("📌 Bot ishga tushdi...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
