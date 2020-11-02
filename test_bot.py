import telebot
import datetime
import sqlite3
import random

def word_combination():
    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM words WHERE genere='adj' ORDER BY RANDOM() LIMIT 1")
    adj = cursor.fetchall()
    #print(adj)
    conn.close()

    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM words WHERE genere !='adj' ORDER BY RANDOM() LIMIT 1")
    word = cursor.fetchall()
    #print(word)
    conn.close()

    noEnd = adj[0][1][:len(adj[0][1])-2]

    if word[0][2] == 'he':
        result = adj[0][1] +" "+ word[0][1]
    elif word[0][2] == 'she':
        result = noEnd +"ая "+ word[0][1]
    elif word[0][2] == 'it':
        result = noEnd +"ое "+ word[0][1]

    return result


decide = ['Да', 'Нет', 'Наверное', 'Духи говорят да', 'Звезды говорят нет', 'Да, если сегодня четное число', 'Нет, если сегоня дождь', '42', 'Ты разольешь кофе', 'Не могу сказать', 'Неопределенно']
bot_description = '''Бот является тестовой площадкой для моих проектов. На данный момент самое интересное в нем - генератор случайных словосочетаний. В планах создание генератора текста при помощий марковских цепей. Можете написать мне свой отзыв или идею для проета. Мои контакты можно найти в разделе "О создателе".'''
dev_description = '''Я Мария Бурдо, студентка стомфака БГМУ и преподаватель Python, HTML, CSS, JS в школе программирования Itgenio. Контакты для связи: \nhttps://t.me/Mariya_Brd \nhttps://vk.com/m.burdo'''



bot = telebot.TeleBot('1448303289:AAEg0b7k-j3i-4G47J6hqh8q44v16cKxwEY')

keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('Помоги решить', 'Брось кубик')
keybord1.row('Случайное словосочетание')
keybord1.row('О создателе', 'О боте')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, давай начинать!', reply_markup=keybord1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'о боте':
        bot.send_message(message.chat.id, bot_description)
    elif message.text.lower() == 'о создателе':
        bot.send_message(message.chat.id, dev_description)
    elif message.text.lower() == 'помоги решить':
        bot.send_message(message.chat.id, random.choice(decide))
    elif message.text.lower() == 'случайное словосочетание':
        bot.send_message(message.chat.id, word_combination().capitalize())
    elif message.text.lower() == 'брось кубик':
        bot.send_message(message.chat.id, random.randint(1, 6))
    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю:(')


bot.polling()