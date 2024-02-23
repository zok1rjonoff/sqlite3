from telebot import types


def number_button():
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    number = types.KeyboardButton("Send phone number", request_contact=True)
    return mark.add(number)


def location_button():
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    location = types.KeyboardButton("Send location", request_location=True)
    return mark.add(location)



