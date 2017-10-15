# -*- coding: utf-8 -*-
from twx.botapi import *
from time import sleep
import pickle
from os import path
import os
import aiml
import traceback
###############################################################################################################3

# Configuração para inciar o bot
CURR_PATH = path.dirname(path.realpath(__file__))
DUMP_FILE = path.join(CURR_PATH, "data.pkl")

token = '401234240:AAGwJPXWF4Iz-g0PQ_JImXQoVbd0Sk6lS8g'
bot = TelegramBot(token)
bot.update_bot_info().wait()
print(bot.username)
last_update_id = 0

os.chdir('C:/Users/Roberto Maier/PycharmProjects/LinaraBot/LinaraBot_AIML/botdata/standard') # diretório que contém os arquivos da AIML standard
ai = aiml.Kernel()# inicialização
ai.learn('startup.xml')  # lê o arquivo principal da AIML e faz referências aos outros
ai.respond('load aiml b')  # faz com que os outros arquivos da AIML sejam carregados

print("Getting updates".center(50, '-'))

def process_message(bot, u):  # This is what we'll do when we get a message

    if u.message.sender and u.message.text and u.message.chat:  # if it is a text message then get it
        chat_id = u.message.chat.id
        user = u.message.sender.username
        message = u.message.text
        updates = message
        resposta_bot =(ai.respond(updates))
        bot.send_message(chat_id, resposta_bot)

while True: #a loop to wait for messages
    updates = bot.get_updates(offset = last_update_id).wait() #we wait for a message
    try:
        for update in updates: #get the messages
            if int(update.update_id) > int(last_update_id): #if it is a new message then get it
                last_update_id = update.update_id
                process_message(bot, update) #send it to the function
                continue
        continue
    except Exception:
        ex = None
        print(traceback.format_exc())
        continue
    sleep(10)