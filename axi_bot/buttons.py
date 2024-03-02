from telebot import types
# import telegram_bot
import database as db


# Кнопка отправки номера
def num_button():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    number = types.KeyboardButton('Отправить номер', request_contact=True)
    # Добавляем кнопку в пространство
    kb.add(number)
    return kb


# Кнопка отправки локации
def loc_button():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    location = types.KeyboardButton('Отправить локацию', request_location=True)
    # Добавляем кнопку в пространство
    kb.add(location)
    return kb


# Кнопки для админ-панели
def admin_buttons():
    # Создаем пространство
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем сами кнопки
    add_pr = types.KeyboardButton('Добавить продукт')
    del_pr = types.KeyboardButton('Удалить продукт')
    edit_pr = types.KeyboardButton('Изменить количество продукта')
    to_menu = types.KeyboardButton('На главную')
    # Объединяем кнопки с пространством
    kb.add(add_pr, edit_pr, del_pr)
    kb.row(to_menu)
    return kb


# Кнопки вывода товара
def main_menu_buttons(all_prods):
    kb = types.InlineKeyboardMarkup(row_width=2)
    prod_buttons = [types.InlineKeyboardButton(text=f'{i[1]}',
                                               callback_data=f'{i[0]}')
                    for i in all_prods if i[2] > 0
                    ]
    cart = types.InlineKeyboardButton(text='Корзина', callback_data='cart')
    kb.add(*prod_buttons)
    kb.row(cart)
    return kb


# Кнопки с выбором количества
def count_buttons(chat_id, users, product, amount=1, plus_or_minus=''):
    quantity = db.get_product_count_by_id(product)[0]
    kb = types.InlineKeyboardMarkup(row_width=3)
    minus = types.InlineKeyboardButton(text='-', callback_data='decrement')
    current_amount = types.InlineKeyboardButton(text=str(amount), callback_data=amount)
    plus = types.InlineKeyboardButton(text='+', callback_data='increment')
    to_cart = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='to_cart')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    if plus_or_minus == 'increment':
        if amount > quantity:
            amount -= 1
            current_amount = types.InlineKeyboardButton(text=str(quantity), callback_data=quantity)
        else:
            users[chat_id]["pr_count"] = users[chat_id]["pr_count"] + 1
            current_amount = types.InlineKeyboardButton(text=str(amount), callback_data=amount)
    elif plus_or_minus == 'decrement':
        if amount > 1:
            users[chat_id]["pr_count"] = users[chat_id]["pr_count"] - 1
            current_amount = types.InlineKeyboardButton(text=str(amount), callback_data=amount)
        else:
            current_amount = types.InlineKeyboardButton(text=str(1), callback_data=1)
    kb.add(minus, current_amount, plus)
    kb.row(to_cart)
    kb.row(back)
    return kb


# Кнопки корзины
def cart_buttons():
    # Создаем пространство
    kb = types.InlineKeyboardMarkup(row_width=2)
    # Создаем сами кнопки
    order = types.InlineKeyboardButton(text='Оформить заказ', callback_data='order')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    clear = types.InlineKeyboardButton(text='Очистить корзину', callback_data='clear')
    # Добавляем кнопки в пространство
    kb.add(clear, back)
    kb.row(order)
    return kb
