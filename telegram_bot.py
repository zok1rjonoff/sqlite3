import buttons
import telebot

# Bot's object was created
bot = telebot.TeleBot("6923031258:AAF9Ar0Rz5mGrxdT003O-i8688v1BtJY3vc")


@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Welcome :)", reply_markup=buttons.menu())


@bot.message_handler(commands=["my_git_hub"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "https://github.com/zok1rjonoff")


@bot.message_handler(content_types=["text"])
def text(message):
    user_id = message.from_user.id

    if message.text.lower() == "From ... to UZS".lower():
        bot.send_message(user_id, f"Welcome:)\n"
                                  f"{buttons.lis_of_ccy} \n"
                                  f"Enter like: ... usd : uzs or USD : UZS")
    elif message.text.lower() == "Dictionary".lower():
        bot.send_message(user_id, f"Available words:\n{buttons.words} \n"
                                  f"Write one them ")
    elif message.text.lower() == "Wikipedia".lower():
        bot.send_message(user_id, f"Available information about programming languages:\n{buttons.wikipedia}\n"
                                  f"Write one them")
    elif "uzs" in message.text:
        string = message.text.split()
        first = string[1].upper()
        second = string[-1].upper()
        money = float(string[0])
        total = buttons.rate(money, first, second)
        bot.send_message(user_id, total, reply_markup=buttons.menu())
    elif message.text.lower() in buttons.wikipedia_dic.keys():
        bot.send_message(user_id, buttons.wikipedia_dic[message.text.lower()], reply_markup=buttons.menu())
    elif message.text.lower() in buttons.dictionary_dic.keys():
        bot.send_message(user_id, buttons.dictionary_dic[message.text.lower()], reply_markup=buttons.menu())
    else:
        bot.send_message(user_id, "Something went wrong")


bot.polling(non_stop=True)
