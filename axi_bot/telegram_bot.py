import telebot
import buttons as bt
import database as db
from geopy import Nominatim

# Создаем объект бота
bot = telebot.TeleBot('7054141581:AAE8-HL9HPXf21BdTtg-U0pbD-RkRNUkIiU')
# Работа с картами
geolocator = Nominatim(
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0')
# id админа
admin_id = 855574466
# Временные данные
users = {}


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    check = db.check_user(user_id)
    prods = db.get_pr()
    if check:
        bot.send_message(user_id, 'Добро пожаловать в наш магазин!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(user_id, 'Выберите товар:',
                         reply_markup=bt.main_menu_buttons(prods))
    else:
        bot.send_message(user_id, 'Здравствуйте! '
                                  'Давайте проведем регистрацию!\n'
                                  'Напишите свое имя',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        # Переход на этап получения имени
        bot.register_next_step_handler(message, get_name)


# Этап получения номера
def get_name(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, 'Супер, а теперь отправьте номер!',
                     reply_markup=bt.num_button())
    # Переход на этап получения номера
    bot.register_next_step_handler(message, get_number, user_name)


# Этап получения номера
def get_number(message, user_name):
    user_id = message.from_user.id
    # Если юзер отправил номер по кнопке
    if message.contact:
        user_number = message.contact.phone_number
        bot.send_message(user_id, 'А теперь локацию!',
                         reply_markup=bt.loc_button())
        # Переход на этап получения локации
        bot.register_next_step_handler(message, get_location,
                                       user_name, user_number)
    # Если юзер отправил номер не по кнопке
    else:
        bot.send_message(user_id, 'Отправьте номер по кнопке!',
                         reply_markup=bt.num_button())
        # Возврат на этап получения номера
        bot.register_next_step_handler(message, get_number, user_name)


# Этап получения локации
def get_location(message, user_name, user_number):
    user_id = message.from_user.id
    # Если юзер отправил локацию по кнопке
    if message.location:
        user_location = geolocator.reverse(f'{message.location.latitude}, '
                                           f'{message.location.longitude}')
        db.register(user_id, user_name, user_number, str(user_location))
        bot.send_message(user_id, 'Регистрация прошла упешно!')
    # Если юзер отправил локацию не по кнопке
    else:
        bot.send_message(user_id, 'Отправьте локацию через кнопку!',
                         reply_markup=bt.loc_button())
        # Возврат на этап получения локации
        bot.register_next_step_handler(message, get_location,
                                       user_name, user_number)


# Выбор количества товара
@bot.callback_query_handler(lambda call: call.data in ['increment', 'decrement', 'to_cart', 'back'])
def choose_pr_amount(call):
    chat_id = call.message.chat.id
    if call.data == 'increment':
        new_amount = users[chat_id]['pr_count']
        product = users[chat_id]["pr_name"]
        new_amount += 1
        bot.edit_message_reply_markup(chat_id=chat_id, message_id=call.message.message_id,
                                      reply_markup=bt.count_buttons(chat_id, users, product, new_amount, 'increment'))
    elif call.data == 'decrement':
        new_amount = users[chat_id]['pr_count']
        product = users[chat_id]["pr_name"]
        new_amount -= 1
        bot.edit_message_reply_markup(chat_id=chat_id, message_id=call.message.message_id,
                                      reply_markup=bt.count_buttons(chat_id, users, product, new_amount, 'decrement'))
    elif call.data == 'back':
        prods = db.get_pr()
        bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
        bot.send_message(chat_id, 'Возвращаю вас обратно в меню',
                         reply_markup=bt.main_menu_buttons(prods))
    elif call.data == 'to_cart':
        product = users[chat_id]["pr_name"]
        price = db.get_exact_pr(users[chat_id]['pr_name'])
        pr_amount = users[chat_id]['pr_count']
        total = price[3] * pr_amount
        db.add_pr_to_cart(chat_id, product, pr_amount, total)
        bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
        bot.send_message(chat_id, 'Товар успешно добавлен в корзину, что хотите сделать?',
                         reply_markup=bt.cart_buttons())


# Корзина
@bot.callback_query_handler(lambda call: call.data in ['cart', 'order', 'back', 'clear'])
def cart_handle(call):
    chat_id = call.message.chat.id

    if call.data == 'cart':
        cart = db.show_cart(chat_id)
        print(cart[0])
        text = f'Ваша корзина\n\n' \
               f'Товар: {cart[1]}\n' \
               f'Количество: {cart[2]}\n' \
               f'Итого: ${cart[3]}'
        bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
        bot.send_message(chat_id, text, reply_markup=bt.cart_buttons())
    elif call.data == 'clear':
        db.clear_cart(chat_id)
        prods = db.get_pr()
        bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
        bot.send_message(chat_id, 'Ваша корзина очищена!',
                         reply_markup=bt.main_menu_buttons(prods))
    elif call.data == 'order':
        prods = db.get_pr()
        cart = db.make_order(chat_id)
        print(f"cart {cart}")
        text = f'Новый заказ!\n\n' \
               f'id пользователя: {cart[0][0]},\n' \
               f'Товар: {cart[0][1]}\n' \
               f'Количество: {cart[0][2]}\n' \
               f'Общая сумма: ${cart[0][3]}\n' \
               f'Адрес: {cart[1]}'
        bot.send_message(admin_id, text)
        bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
        bot.send_message(chat_id, 'Заказ успешно оформлен, специалисты с вами свяжутся!',
                         reply_markup=bt.main_menu_buttons(prods))
    elif call.data == 'back':
        prods = db.get_pr()
        bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
        bot.send_message(chat_id, 'Возвращаю вас обратно в меню',
                         reply_markup=bt.main_menu_buttons(prods))


# Вывод инфы о продукте
@bot.callback_query_handler(lambda call: db.get_exact_pr(call.data))
def get_product(call):
    product_id = call.data
    chat_id = call.message.chat.id
    exact_product = db.get_exact_pr(call.data)
    users[chat_id] = {'pr_name': product_id, 'pr_count': 1}
    bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
    bot.send_photo(chat_id, photo=exact_product[4],
                   caption=f'{exact_product[0]},\n\n'
                           f'Описание товара: {exact_product[1]}\n'
                           f'Количество товара: {exact_product[2]}\n'
                           f'Цена товара: {exact_product[3]}',
                   reply_markup=bt.count_buttons(chat_id, users, product_id))


# Обработка команды /admin
@bot.message_handler(commands=['admin'])
def admin(message):
    if message.from_user.id == admin_id:
        bot.send_message(admin_id, 'Добро пожаловать в админ-панель!',
                         reply_markup=bt.admin_buttons())
        # Переход на этап выбора команды
        bot.register_next_step_handler(message, admin_choice)
    else:
        bot.send_message(message.from_user.id, 'Вы не админ!\n'
                                               'Нажмите /start')


# Этап выбора команды админом
def admin_choice(message):
    if message.text == 'Добавить продукт':
        bot.send_message(admin_id, 'Итак, давайте начнем! Введите название товара',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        # Переход на этап получения названия
        bot.register_next_step_handler(message, get_pr_name)
    elif message.text == 'Удалить продукт':
        pr_check = db.check_pr()
        if pr_check:
            bot.send_message(admin_id, 'Введите id товара')
            # Переход на этап получения id товара
            bot.register_next_step_handler(message, get_pr_to_del)
        else:
            bot.send_message(admin_id, 'Продуктов нет!')
            # Возвращаем на этап выбора команды
            bot.register_next_step_handler(message, admin_choice)
    elif message.text == 'Изменить количество продукта':
        pr_check = db.check_pr()
        if pr_check:
            bot.send_message(admin_id, 'Введите id товара')
            # Переход на этап получения id товара
            bot.register_next_step_handler(message, get_pr_to_edit)
        else:
            bot.send_message(admin_id, 'Продуктов нет!')
            # Возвращаем на этап выбора команды
            bot.register_next_step_handler(message, admin_choice)
    elif message.text == "На главную":
        products = db.get_pr()
        bot.send_message(message.from_user.id, "Список товаров", reply_markup=bt.main_menu_buttons(products))


# Этап получения названия
def get_pr_name(message):
    pr_name = message.text
    bot.send_message(admin_id, 'Теперь придумайте описание товару!')
    # Переход на этап получения описания
    bot.register_next_step_handler(message, get_pr_description, pr_name)


# Этап получения описания
def get_pr_description(message, pr_name):
    pr_description = message.text
    bot.send_message(admin_id, 'Какое количество товара?')
    # Переход на этап получения количества
    bot.register_next_step_handler(message, get_pr_count,
                                   pr_name, pr_description)


# Этап получения количества
def get_pr_count(message, pr_name, pr_description):
    # Проверка на тип данных
    if message.text.isnumeric() is not True:
        bot.send_message(admin_id, 'Пишите только целые числа!')
        # Возвращаем на этап получения количества
        bot.register_next_step_handler(message, get_pr_count,
                                       pr_name, pr_description)
    else:
        pr_count = int(message.text)
        bot.send_message(admin_id, 'Какая цена у товара?')
        # Переход на этап получения цены
        bot.register_next_step_handler(message, get_pr_price,
                                       pr_name, pr_description, pr_count)


# Этап получения цены
def get_pr_price(message, pr_name, pr_description, pr_count):
    # Проверка на тип данных
    if message.text.isdecimal() is not True:
        bot.send_message(admin_id, 'Пишите только дробные числа!')
        # Возвращаем на этап получения количества
        bot.register_next_step_handler(message, get_pr_price,
                                       pr_name, pr_description, pr_count)
    else:
        pr_price = float(message.text)
        bot.send_message(admin_id, 'Последний этап, зайдите на сайт '
                                   'https://postimages.org/ и загрузите туда фото.\n'
                                   'Затем, отправьте мне прямую ссылку на фото!')
        # Переход на этап получения фото
        bot.register_next_step_handler(message, get_pr_photo,
                                       pr_name, pr_description, pr_count, pr_price)


# Этап получения фото
def get_pr_photo(message, pr_name, pr_description, pr_count, pr_price):
    pr_photo = message.text
    db.add_pr(pr_name, pr_description, pr_count, pr_price, pr_photo)
    bot.send_message(admin_id, 'Готово! Что-то ещё?',
                     reply_markup=bt.admin_buttons())
    # Переход на этап выбора команды
    bot.register_next_step_handler(message, admin_choice)


# Изменение продукта
def get_pr_to_edit(message):
    # Проверка на тип данных
    if message.text.isnumeric() is not True:
        bot.send_message(admin_id, 'Пишите только целые числа!')
        # Возвращаем на этап получения id товара
        bot.register_next_step_handler(message, get_pr_to_edit)
    else:
        pr_id = int(message.text)
        bot.send_message(admin_id, 'Сколько товара прибыло?')
        # Переход на этап получения стока
        bot.register_next_step_handler(message, get_pr_stock, pr_id)


# Этап получения стока
def get_pr_stock(message, pr_id):
    # Проверка на тип данных
    if message.text.isnumeric() is not True:
        bot.send_message(admin_id, 'Пишите только целые числа!')
        # Возвращаем на этап получения стока
        bot.register_next_step_handler(message, get_pr_stock, pr_id)
    else:
        pr_stock = int(message.text)
        db.change_pr_count(pr_id, pr_stock)
        bot.send_message(admin_id, 'Количество товара успешно изменено!',
                         reply_markup=bt.admin_buttons())
        # Переход на этап получения выбора команды
        bot.register_next_step_handler(message, admin_choice)


# Удаление продукта
def get_pr_to_del(message):
    # Проверка на тип данных
    if message.text.isnumeric() is not True:
        bot.send_message(admin_id, 'Пишите только целые числа!')
        # Возвращаем на этап получения id товара
        bot.register_next_step_handler(message, get_pr_to_del)
    else:
        pr_id = int(message.text)
        db.del_pr(pr_id)
        bot.send_message(admin_id, 'Товар успешно удален!',
                         reply_markup=bt.admin_buttons())
        # Переход на этап получения выбора команды
        bot.register_next_step_handler(message, admin_choice)


# Запуск бота
bot.polling()
