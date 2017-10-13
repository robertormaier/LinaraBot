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

os.chdir('C:/Users/Roberto Maier/PycharmProjects/LinaraBot/LinaraBot_AIML/botdata/standard') # diretório que contém os arquivos da AIML standard
ai = aiml.Kernel()# inicialização
ai.learn('startup.xml')  # lê o arquivo principal da AIML e faz referências aos outros
ai.respond('load aiml b')  # faz com que os outros arquivos da AIML sejam carregados

print("Getting updates".center(50, '-'))

while (1 == 1):
    updates = bot.get_updates().wait()
    #update = input('Fale algo ao bot em english:')
    resposta_bot = ("Resposta do bot: %s" % ai.respond(updates))
    print('Resposta recebida',updates)
    print(resposta_bot)

    sleep(2)