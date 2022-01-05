from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bot.data import for_user_registration
from bot.states import ListCreation
from bot.keyboards import inline


async def create_deal_list(callback : types.CallbackQuery):
    await callback.message.answer("Как вы хотите назвать этот список?")
    await ListCreation.name.set()


async def get_list_name(message: types.Message,state : FSMContext):
    await for_user_registration.add_list(message.from_user.id, message.text)
    await message.answer("Список был успешно создан")
    await message.answer("Все списки дел: ", reply_markup=inline.create_list_of_lists())
    await state.finish()


def register_list_handler(dp: Dispatcher):
    dp.register_callback_query_handler(create_deal_list, text="create_list")
    dp.register_message_handler(get_list_name,state=ListCreation.name)