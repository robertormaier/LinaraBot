# -*- coding: utf-8 -*-

from twx.botapi import TelegramBot
from time import sleep
import pickle
import mysql
from os import path

# Configuração para inciar o bot
CURR_PATH = path.dirname(path.realpath(__file__))
DUMP_FILE = path.join(CURR_PATH,"data.pkl")

cnx = mysql.connector.connect(user='scott', password='tiger',
                              host='127.0.0.1',
                              database='employees')
cnx.close()

BOTAPI = ''
bot = TelegramBot(BOTAPI)
bot.update_bot_info().wait()

print  (bot.username)

if path.exists(DUMP_FILE):  # Se existe, carregar a lista de mensagens respondidas
    pkl_file = open(DUMP_FILE)
    answered_messages = pickle.load(pkl_file)
else:
    answered_messages = []

_bot_message = {'Oi, eu sou um bot, meu nome é Linara, e o seu? Em breve terei mais funcionalidades!'}

while (True):
    print ("Getting updates".center(50, '-'))

    updates = bot.get_updates().wait()
    for pos, update in enumerate(updates):

        print(str(pos) + " " + str(update) + "n")

        update_id = update.update_id
        if (update_id not in answered_messages):  # Se a mensagem não foi respondida, responda o usuário
            sender_id = update.message.sender.id
            result = bot.send_message(sender_id, _bot_message).wait()

            print(result)

            if (result):
                answered_messages.append(update_id)
    output = open(DUMP_FILE, 'wb')
    pickle.dump(answered_messages, output)  # persiste a lista de mensagens respondidas
    sleep(10)
