import telebot

bot = telebot.TeleBot('6648964856:AAEl3d48O2kL71dxEpFrK8CAgL2Oy9kLkoY')


from telebot import types

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Начать работу!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Для продолжения нажми на кнопку ниже, так мы проверяем вас на робота!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Начать работу!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Поиск')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '❓ Выберите что-то из предложенного ниже.', reply_markup=markup) #ответ бота

bot.polling(none_stop=True, interval=0)

