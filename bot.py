# -*- coding: utf-8 -*-
import redis
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
import telebot
import telepot
import time
import urllib3


bot_token = '1697731247:AAEIF2FTUqIPcOQCUsSNonRsw4HtGWNTdRU'   #t.me/test_ju_18bot
# chat id -470178599
bot = telebot.TeleBot(token = bot_token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message,'Coucou')

@bot.message_handler(commands=['groscon'])
def welcome(message):
    bot.reply_to(message,'Ta gueule')



"""
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
        if message.from_user.first_name =="julien":
            bot.send_message(1685295937, 'tu as recu un message de la petite patate dans la conversation avec le robot !')

"""
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)

@bot.message_handler(regexp="aime")
def handle_message(message):
	bot.reply_to(message,'Oui moi aussi !')

@bot.message_handler(regexp="julien")
def handle_message(message):
    bot.forward_message(1320049636, -470178599, message.id)

bot.polling(none_stop=True, interval=0, timeout=20)
