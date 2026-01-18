import telebot.async_telebot as async_telebot
import aiohttp
import asyncio

BOT_TOKEN = "8267814556:AAH6POJPc7oPXnRlht-PZkWc5VUz90xVBVE"
API = "b9fea739fc7ef607bce1fef35c2bfeab"

bot = async_telebot.AsyncTeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, "Shahar nomini yuboring 🌤")

@bot.message_handler(func=lambda m: True)
async def weather(message):
    city = message.text
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"
    

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()

            temp = data['main']['temp']

            if temp > 10:
                holat = "Issiq 🔥"
            elif 2 <= temp <= 10:
                holat = "Iliq 🌤"
            else:
                holat = "Sovuq ❄"

            await bot.send_message(message.chat.id, f"🌍 {city}\n🌡 Harorat: {temp}°C\n☁ Holati: {holat}")
            await bot.send_message(message.chat.id, "Yana shahar nomini yuboring 🌤")

asyncio.run(bot.polling())