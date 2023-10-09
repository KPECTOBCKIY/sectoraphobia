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
        btn2 = types.KeyboardButton('Аккаунт')
        btn3 = types.KeyboardButton('Помощь')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Выберите что-то из предложенного ниже.', reply_markup=markup) #ответ бота

elif message.text == 'Поиск':
    bot.send_message(message.from_user.id, '👁️ Вы можете выполнить поиск следующим способом:\n\n📞 По номеру телефона: +79991231212\n📝По телеграм айди или юзернейму: @UserOsint, 1545524566\n\n📣 Используйте только проверенные сервисы по типу нашего, отличный OSINT инструмент.')

bot.polling(none_stop=True, interval=0)

