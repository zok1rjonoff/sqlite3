import telebot
import axi_market_buttons
import database
from geopy import Nominatim

# Создаем объект бота
bot = telebot.TeleBot("7054141581:AAE8-HL9HPXf21BdTtg-U0pbD-RkRNUkIiU")
# Работа с картами
geolocator = Nominatim(
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0')


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    check = database.check_user(user_id)
    if check:
        bot.send_message(user_id, 'Добро пожаловать в наш магазин!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
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
                     reply_markup=axi_market_buttons.number_button())
    # Переход на этап получения номера
    bot.register_next_step_handler(message, get_number, user_name)


# Этап получения номера
def get_number(message, user_name):
    user_id = message.from_user.id
    # Если юзер отправил номер по кнопке
    if message.contact:
        user_number = message.contact.phone_number
        bot.send_message(user_id, 'А теперь локацию!',
                         reply_markup=axi_market_buttons.location_button())
        # Переход на этап получения локации
        bot.register_next_step_handler(message, get_location,
                                       user_name, user_number)
    # Если юзер отправил номер не по кнопке
    else:
        bot.send_message(user_id, 'Отправьте номер по кнопке!',
                         reply_markup=axi_market_buttons.number_button())
        # Возврат на этап получения номера
        bot.register_next_step_handler(message, get_number, user_name)


# Этап получения локации
def get_location(message, user_name, user_number):
    user_id = message.from_user.id
    # Если юзер отправил локацию по кнопке
    if message.location:
        user_location = geolocator.reverse(f'{message.location.longitude}, '
                                           f'{message.location.latitude}')
        database.registration(user_id, user_name, user_number, user_location)
        bot.send_message(user_id, 'Регистрация прошла упешно!')
    # Если юзер отправил локацию не по кнопке
    else:
        bot.send_message(user_id, 'Отправьте локацию через кнопку!',
                         reply_markup=axi_market_buttons.location_button())
        # Возврат на этап получения локации
        bot.register_next_step_handler(message, get_location,
                                       user_name, user_number)


bot.polling()
