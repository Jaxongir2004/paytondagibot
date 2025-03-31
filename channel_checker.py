from aiogram import Bot
import asyncio

TOKEN = "7630943846:AAHSU1nfcYVftaTlxbADp2L__UGSii2M4lE"
CHANNEL_ID = "@allalaassa"
BOT_ID = 7630943846  # Botning ID sini to‘g‘ri qo‘y

async def check_channel_messages():
    bot = Bot(token=TOKEN)
    try:
        messages = await bot.get_chat(CHANNEL_ID)
        print(messages)
    finally:
        await bot.session.close()

asyncio.run(check_channel_messages())
