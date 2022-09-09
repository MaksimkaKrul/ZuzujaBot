import random
import emoji
from telebot import types
from setings import bot
from pathlib import Path

time_for_message = {}
rps_game = ['камінь', 'папір', 'ножниці']


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Список команд доступних у боті: \n"
                          "/discordannouncement - дізнатись 3 останніх оголошення з діскорд каналу GoITeens \n"
                          "/rock_paper_scissors  - зіграти в камінь, ножниці, папір з ботом \n"
                          "/discordnews - дізнатись 3 останніх новини GoITeens" )


@bot.message_handler(commands=['discordannouncement'])
def get_announcement(message):
    last_announcement = Path('lastmessage1.txt').read_text()
    last_announcement = emoji.emojize(last_announcement)
    bot.reply_to(message, "Зараз ви дізнаєтесь останні 3 оголошення discord сервера GoITeens, "
                          "кожне оголошення відокремлене знаками ----")
    bot.reply_to(message, last_announcement)


@bot.message_handler(commands=['rock_paper_scissors'])
def get_answer(message):
    keyboard = types.InlineKeyboardMarkup()
    key_rock = types.InlineKeyboardButton(text='Камінь 💎', callback_data='rock')
    keyboard.add(key_rock)
    key_paper = types.InlineKeyboardButton(text='Папір 📃', callback_data='paper')
    keyboard.add(key_paper)
    key_scissors = types.InlineKeyboardButton(text='Ножниці ✂', callback_data='scissors')
    keyboard.add(key_scissors)
    question = 'Щоб почати гру, вибери камінь,папір чи ножниці'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot_choice = random.choice(rps_game)
    bot.send_message(call.message.chat.id, 'Я обрав' + ' ' + bot_choice)
    if call.data == "rock":
        if bot_choice == 'камінь':
            bot.send_message(call.message.chat.id, 'У нас нічия!')
        elif bot_choice == 'папір':
            bot.send_message(call.message.chat.id, 'Ти програв!')
        else:
            bot.send_message(call.message.chat.id, 'Ти переміг!')

    elif call.data == "paper":
        if bot_choice == 'камінь':
            bot.send_message(call.message.chat.id, 'Ти переміг!')
        elif bot_choice == 'папір':
            bot.send_message(call.message.chat.id, 'У нас нічия!')
        else:
            bot.send_message(call.message.chat.id, 'Ти програв!')

    elif call.data == "scissors":
        if bot_choice == 'камінь':
            bot.send_message(call.message.chat.id, 'Ти програв!')
        elif bot_choice == 'папір':
            bot.send_message(call.message.chat.id, 'У нас виграв!')
        else:
            bot.send_message(call.message.chat.id, 'У нас нічия!')


@bot.message_handler(commands=['discordnews'])
def get_news(message):
    last_news = Path('lastmessage2.txt').read_text()
    last_news = emoji.emojize(last_news)
    bot.reply_to(message, "Зараз ви дізнаєтесь останні 3 новини discord сервера GoITeens, "
                          "кожна новина відокремлена знаками ----")
    bot.reply_to(message, last_news)

bot.infinity_polling()
