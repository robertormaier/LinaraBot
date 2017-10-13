# -*- coding: utf-8 -*-

from twx.botapi import TelegramBot
from time import sleep
import pickle
from os import path
import os
import aiml

###############################################################################################################3

# Configuração para inciar o bot
CURR_PATH = path.dirname(path.realpath(__file__))
DUMP_FILE = path.join(CURR_PATH, "data.pkl")

token = '401234240:AAGwJPXWF4Iz-g0PQ_JImXQoVbd0Sk6lS8g'
bot = TelegramBot(token)
bot.update_bot_info().wait()
print(bot.username)

os.chdir('C:/Users/Roberto Maier/PycharmProjects/LinaraBot/LinaraBot_AIML/aiml')  # diretório que contém os arquivos da AIML standard
ai = aiml.Kernel()# inicialização
ai.learn('std-startup.xml')  # lê o arquivo principal da AIML e faz referências aos outros
ai.respond('load aiml b')  # faz com que os outros arquivos da AIML sejam carregados

while (1 == 1):
    frase = input('Fale algo ao bot em english:')
    print ("Resposta do bot: %s" % ai.respond(frase))


if path.exists(DUMP_FILE):  # Se existe, carregar a lista de mensagens respondidas
    pkl_file = open(DUMP_FILE, 'rb')
    answered_messages = pickle.load(pkl_file)
else:
    answered_messages = []

_bot_message = {'Oi, eu sou um bot, meu nome é Linara, e o seu? Em breve terei mais funcionalidades!'}

while (True):
    print("Getting updates".center(50, '-'))

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
