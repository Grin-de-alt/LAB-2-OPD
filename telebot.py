import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command



# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5768772566:AAFwovlobfH9I79-dpoV4OizxdA12_s-yMs")
# Диспетчер
dp = Dispatcher()

with open('questions.txt', encoding="utf-8") as f:
 answer = f.read().split('\n')

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello, i'm your personal FAQ-bot!")
    await message.answer("Write '/FAQ' to get started.")
@dp.message(Command("FAQ"))
async def cmd_start(message: types.Message):
    await message.answer("Here the list of most popular questions,\n""Write number one of them to get the answer.")
    await message.answer("1.Когда выдаются студенческие билеты?\n""2.Когда выдаются зачетные книжки?\n""3.Как и когда оформляется банковская карточка?\n""4.Как и когда в библиотеке выдаются учебники?\n""5.Как получить справку о том, что «я здесь учусь»?\n""6.Как получить справку для военкомата о предоставлении отсрочки от службы в армии?\n""7.Как проходит сессия?\n""8.Какие формы проверки знаний студентов возможны? \n""9.Как узнать вид промужуточной аттестации по предмету и перечень мероприятий промежуточной аттестации, которые предстоит сдавать в будущую сессию? \n""10.Какой студент считается неуспевающим?\n""11.При каких условиях студенты допускаются к сдаче экзаменов? Может ли студент, не сдавший зачеты, быть допущен к экзамену?\n""12.Какие документы студент обязан иметь при себе на экзамене?\n""13.Каковы правила пересдачи экзамена с оценкой 'неудовлетворительно'?\n""14.При наличии какого количества задолженностей студент представляется к отчислению за академическую неуспеваемость?\n""15.Правда ли, что посещение занятий в вузе не является обязательным? \n""16.Каковы права и обязанности старосты группы? \n""17.Как поступить при утере документов (студенческий билет, зачетная книжка)?\n")
@dp.message()
async def cmd_start(message: types.Message):
    global i
    i = message.text
    await message.reply(answer[int(i)-1])
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
