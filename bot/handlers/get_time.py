from aiogram import types, Dispatcher
from bot.data import for_user_registration
from bot.keyboards import inline
from bot.states import TaskCreation, ListCreation
from aiogram.dispatcher import FSMContext
from datetime import time



async def get_time(message: types.Message,state : FSMContext):
    try:
        set_time: time = time.fromisoformat(message.text)
    except ValueError:
        return await message.answer("Введено некорректное время:(")
    for_user_registration.add_task(TaskCreation.list_id, TaskCreation.title, TaskCreation.disc, TaskCreation.date, set_time)
    await message.answer("Задача успешно добавлена !!!", reply_markup=inline.listMenu)
    await state.finish()
    await ListCreation.actionwithmenu.set()


def register_get_time(dp: Dispatcher):
    dp.register_message_handler(get_time, state=TaskCreation.get_time)