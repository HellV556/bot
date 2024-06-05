import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import random


bot = Bot(token="7347274099:AAGNM8iTtW7T78ymYRTrT86ZB8Yg6_-lsuI")
dp = Dispatcher()
score=0
questions={
    'кто создал python':
        [
        [types.KeyboardButton(text="Гвидо ван Россум")],
        [types.KeyboardButton(text="Сережа Дебус")],
        [types.KeyboardButton(text="норм чел")],
        [types.KeyboardButton(text="плохой ответ")]
        ],
    'сколько бит в байте':
        [
        [types.KeyboardButton(text="0")],
        [types.KeyboardButton(text="1024")],
        [types.KeyboardButton(text="3")],
        [types.KeyboardButton(text="8")]
        ],
    "корень из 4":
        [
        [types.KeyboardButton(text="4")],
        [types.KeyboardButton(text="10000")],
        [types.KeyboardButton(text="+-2")],
        [types.KeyboardButton(text="52")]
        ],
    "библиотека с помощью которой был создан этот бот":
        [
        [types.KeyboardButton(text="random")],
        [types.KeyboardButton(text="aiogram")],
        [types.KeyboardButton(text="telegram")],
        [types.KeyboardButton(text="flask")]
        ],
    "дисциплина в рамках которой был создан этот бот":
        [
        [types.KeyboardButton(text="ОРГ")],
        [types.KeyboardButton(text="ОБЖ")],
        [types.KeyboardButton(text="Основы проф. деятельности")],
        [types.KeyboardButton(text="Математика")]
        ]
    }
@dp.message(Command("start"))
@dp.message(F.text=='Заново')
async def cmd_start(message: types.Message):
    question=random.choice(list(questions))
    kb = questions[question]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    questions.pop(question)
    await message.answer(question, reply_markup=keyboard)
@dp.message(lambda message: message.text in ["Продолжить"])
async def cmd_start(message: types.Message):
    global questions,score
    if questions:
        question=random.choice(list(questions))
        kb = questions[question]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
        questions.pop(question)
    else:
        question=f"Игра окончена, ваш счет{score} Желаете повторить?"
        kb=[[types.KeyboardButton(text="Занаво")]]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
        score=0
        questions={
    'кто создал python':
        [
        [types.KeyboardButton(text="Гвидо ван Россум")],
        [types.KeyboardButton(text="Сережа Дебус")],
        [types.KeyboardButton(text="норм чел")],
        [types.KeyboardButton(text="плохой ответ")]
        ],
    'сколько бит в байте':
        [
        [types.KeyboardButton(text="0")],
        [types.KeyboardButton(text="1024")],
        [types.KeyboardButton(text="3")],
        [types.KeyboardButton(text="8")]
        ],
    "корень из 4":
        [
        [types.KeyboardButton(text="4")],
        [types.KeyboardButton(text="10000")],
        [types.KeyboardButton(text="+-2")],
        [types.KeyboardButton(text="52")]
        ],
    "библиотека с помощью которой был создан этот бот":
        [
        [types.KeyboardButton(text="random")],
        [types.KeyboardButton(text="aiogram")],
        [types.KeyboardButton(text="telegram")],
        [types.KeyboardButton(text="flask")]
        ],
    "дисциплина в рамках которой был создан этот бот":
        [
        [types.KeyboardButton(text="основы проф.деятельности")],
        [types.KeyboardButton(text="программирование")],
        [types.KeyboardButton(text="теория автоматов")],
        [types.KeyboardButton(text="орг")]
        ]
    }
    await message.answer(question, reply_markup=keyboard)

@dp.message(lambda message: message.text in ["Гвидо ван Россум", "+-2", "основы проф.деятельности" ,"aiogram"  ,"8"])
async def correct(message: types.Message):
    global score
    score+=1
    kb=[[types.KeyboardButton(text="Продолжить")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb) 
    await message.reply(f"правильно! Ваш счёт: {score}",reply_markup=keyboard)

@dp.message(lambda message: message.text not in ["Гвидо ван Россум", "основы проф.деятельности", "+-2" ,"aiogram"  ,"8"])
async def incorrect(message: types.Message):
    global score
    kb=[[types.KeyboardButton(text="Продолжить")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    #keyboard.add(kb)
    await message.reply(f"Не правильно! Ваш счёт: {score}",reply_markup=keyboard)
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())