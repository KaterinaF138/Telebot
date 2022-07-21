

import telebot
from telebot import types  # импорт библ кнопок
import bs4  # установили библиотекуа для парсинга
import urllib  # получить его html-код сайта

site = urllib.request.urlopen('https://kogda.by/routes/brest/autobus').read()
soup = bs4.BeautifulSoup(site, features="html.parser")
raw_excersises = soup.find('div', {"class": "routes-block collapse in"})  # забираем интересующий нас кусок кода
excersises = raw_excersises.find_all('a')  # забираем непосредственно блоки с ссылками
links_to_excersises = []  # заводим список для ссылок
for i in range(len(excersises)):  # перебираем список
    links_to_excersises.append(excersises[i].get('href'))  # состоящий только из ссылок href
print('I have a list')
print(links_to_excersises)

# print(soup.prettify()) #вывели в консоль html-код сайта, чтоб найти кусок raw_excersises

token = '5582436267:AAEmXVSH8aDkuNqP8K0EOdupfhfEn8iCyBk'
bot = telebot.TeleBot(token)  # объявили бота, передали токен


def create_keyboard():  # функция для создания  кнопок
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    A15A_btn = types.InlineKeyboardButton(text="15 - A", callback_data='1')
    A15B_btn = types.InlineKeyboardButton(text="15 - Б", callback_data='2')
    A15V_btn = types.InlineKeyboardButton(text="15 - В", callback_data='3')
    A23_btn = types.InlineKeyboardButton(text="23", callback_data='4')
    A23A_btn = types.InlineKeyboardButton(text="23 - А", callback_data='5')
    A18_btn = types.InlineKeyboardButton(text="18", callback_data='6')
    keyboard.add(A15A_btn, A15B_btn, A15V_btn)  # добавляем кнопки в список (в один ряд)
    keyboard.add(A23_btn, A23A_btn)
    keyboard.add(A18_btn)
    return keyboard  # возвращаем функцию


@bot.message_handler(commands=['start'])  # чтоб функция срабатывала при команде старт
def start_bot(message):  # функция срабатывает при запуске
    keyboard = create_keyboard()  # создаем кнопки
    bot.send_message(  # дали сообщение боту на отправку кнопки сообщения
        message.chat.id,
        "Куда едем! Введите номер автобуса, без пробела! Через /", reply_markup=keyboard)  # и добавили кнопки


@bot.message_handler(commands=['15А', '15а'])
def send_task(message):
    keyboard = create_keyboard()
    bot.reply_to(message, f'15 - A — {links_to_excersises[18]}', reply_markup=keyboard)


@bot.message_handler(commands=['15Б', '15б'])
def send_task(message):
    keyboard = create_keyboard()
    bot.reply_to(message, f'15 - Б — {links_to_excersises[19]}', reply_markup=keyboard)


@bot.message_handler(commands=['15В', '15в'])
def send_task(message):
    keyboard = create_keyboard()
    bot.reply_to(message, f'15 - В — {links_to_excersises[20]}', reply_markup=keyboard)


@bot.message_handler(commands=['23'])
def send_task(message):
    keyboard = create_keyboard()
    bot.reply_to(message, f'23— {links_to_excersises[30]}', reply_markup=keyboard)


@bot.message_handler(commands=['23А', '23а'])
def send_task(message):
    keyboard = create_keyboard()
    bot.reply_to(message, f'23-А— {links_to_excersises[30]}', reply_markup=keyboard)


@bot.message_handler(commands=['18'])
def send_task(message):
    keyboard = create_keyboard()
    bot.reply_to(message, f'18 — {links_to_excersises[23]}', reply_markup=keyboard)


if __name__ == "__main__":  # запускаем бота
    bot.polling(none_stop=True)
