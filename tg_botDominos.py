from config import token
from aiogram import Bot, Dispatcher, executor, types
import json
from aiogram.dispatcher.filters import Text

bot = Bot(token="Yourtoken", parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_button = ["Pizzas", "News"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_button)

    await message.answer("Welcom to Dominos.by", reply_markup=keyboard)


@dp.message_handler(Text(equals="Pizzas"))
async def get_pizza(message: types.Message):
    with open("pizza.json") as file:
        pizz_dict = json.load(file)

    for k, v in pizz_dict.items():
        pizz = f"<b>{v['name']}</b>\n<a href={v['image']}>&#8203;</a>\n{v['consist']}\n<b><u>{v['cosht']}</u></b>"
        await message.answer(pizz)
    await message.delete()


@dp.message_handler(Text(equals="News"))
async def get_news(message: types.Message):
    with open("news.json") as file:
        news_dict = json.load(file)

    for k, v in news_dict.items():
        news = f"{v['news']}\n<a href={v['link_image']}>&#8203;</a>"
        await message.answer(news)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp)
