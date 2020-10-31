import telebot
import datetime
import random
from helpers import word_combination, holland_combination

decide = ['Да', 'Нет', 'Наверное', 'Духи говорят да', 'Звезды говорят нет', 'Да, если сегодня четное число', 'Нет, если сегоня дождь', '42', 'Ты разольешь кофе', 'Не могу сказать', 'Неопределенно', 'Мой код говно']

bot = telebot.TeleBot('1448303289:AAEg0b7k-j3i-4G47J6hqh8q44v16cKxwEY')

keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('Помоги решить', 'Как я выгляжу?')
keybord1.row('Голландская игра')
keybord1.row('Дата', 'Время', 'День недели')
keybord1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, давай начинать!', reply_markup=keybord1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'И тебе привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'И тебе пока!')
    elif message.text.lower() == 'дата':
        bot.send_message(message.chat.id, datetime.datetime.today().strftime('%d.%m.%Y'))
    elif message.text.lower() == 'время':
        bot.send_message(message.chat.id, datetime.datetime.today().strftime('%H:%M:%S'))
    elif message.text.lower() == 'день недели':
        bot.send_message(message.chat.id, datetime.datetime.today().strftime('%A'))
    elif message.text.lower() == 'помоги решить':
        bot.send_message(message.chat.id, random.choice(decide))
    elif message.text.lower() == 'как я выгляжу?':
        bot.send_message(message.chat.id, 'Как '+word_combination())
    elif message.text.lower() == 'голландская игра':
        bot.send_message(message.chat.id, holland_combination())


bot.polling()