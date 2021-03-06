from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from bot.services.database.commands.list import all_lists
from bot.services.database.commands.task import all_tasks

# Buttons, menu for MainMenu

create_list = InlineKeyboardButton(text='Создать список', callback_data='create_list')
add_task = InlineKeyboardButton(text='Добавить задачу', callback_data='add_task')
lists = InlineKeyboardButton(text='Просмотреть текущие списки задач', callback_data='lists')
tasks_for_day = InlineKeyboardButton(text='Просмотреть все задачи на сегодня', callback_data='tasks_for_day')
motivation_mode = InlineKeyboardButton(text='Режим мотивационных цитат', callback_data='motivational_mode')
bored_mode = InlineKeyboardButton(text='Режим "мне скучно"', callback_data='bored_mode')

menu = InlineKeyboardMarkup()
menu.add(create_list, add_task)
menu.add(lists)
menu.add(tasks_for_day)
menu.add(motivation_mode)
menu.add(bored_mode)

list_cb = CallbackData('list', 'action')

listMenu = InlineKeyboardMarkup(row_width=1)
show_deals = InlineKeyboardButton(text="Посмотреть все задачи", callback_data=list_cb.new(action="show_deals"))
add_deals = InlineKeyboardButton(text="Добавить задачу", callback_data=list_cb.new(action="add_deals"))
do_deals = InlineKeyboardButton(text="Сделать задачу", callback_data=list_cb.new(action="do_deals"))
edit_deal = InlineKeyboardButton(text="Редактировать задачу", callback_data=list_cb.new(action="edit_deal"))
delete_deal = InlineKeyboardButton(text="Удалить задачу", callback_data=list_cb.new(action="delete_deal"))
delete_list = InlineKeyboardButton(text="Завершить работу со списком", callback_data=list_cb.new(action="exit_list"))
listMenu.add(show_deals, add_deals, do_deals, edit_deal, delete_deal, delete_list)

list_main = InlineKeyboardMarkup(row_width=2)
list_main_cb = CallbackData('title', 'action')
back_to_list_menu = InlineKeyboardButton(text="Вернуться в меню списка",
                                         callback_data=list_main_cb.new(action="backtolistmenu"))
back_to_main_menu = InlineKeyboardButton(text="Вернуться в главное меню",
                                         callback_data=list_main_cb.new(action="backtomainmenu"))
list_main.add(back_to_main_menu, back_to_list_menu)

task_cb = CallbackData('name', 'action')

editingTaskMenu = InlineKeyboardMarkup(row_width=1)
edit_title = InlineKeyboardButton(text="Редактировать название задачи", callback_data=task_cb.new(action="edit_title"))
edit_disc = InlineKeyboardButton(text="Редактировать описание задачи", callback_data=task_cb.new(action="edit_disc"))

editingTaskMenu.add(edit_title, edit_disc)


bored_mode_menu = InlineKeyboardMarkup()
bored_mode_menu.add(InlineKeyboardButton(text='Спасибо', callback_data='menu'))
bored_mode_menu.add(InlineKeyboardButton(text='Хочу другое задание', callback_data='another_task'))


start_menu = InlineKeyboardMarkup()
start_menu.add(InlineKeyboardButton(text='Да', callback_data='authorize'))
start_menu.add(InlineKeyboardButton(text='Нет', callback_data='start_add_user'))


def create_list_of_lists(user_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 1
    for key, values in all_lists(user_id).items():
        keyboard.add(InlineKeyboardButton(text=key, callback_data=values))
    return keyboard


def create_list_of_tasks(user_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 1
    for key, values in all_tasks(user_id).items():
        keyboard.add(InlineKeyboardButton(text=key, callback_data=values))
    return keyboard
