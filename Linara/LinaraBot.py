# -*- coding: utf-8 -*-

from twx.botapi import *
import os
import aiml
import traceback
from pyowm import OWM  # Weather API

token = '401234240:AAGwJPXWF4Iz-g0PQ_JImXQoVbd0Sk6lS8g'
OWMKEY = '39961c337fa3338e7e78be19f078ec4e'
bot = TelegramBot(token)
bot.update_bot_info().wait()
print(bot.username)
last_update_id = 0

os.chdir(
    'C:/Users/Roberto Maier/PycharmProjects/LinaraBot/LinaraBot_AIML/botdata/standard')  # diretório que contém os arquivos da AIML standard
ai = aiml.Kernel()  # inicialização
ai.learn('startup.xml')  # lê o arquivo principal da AIML e faz referências aos outros
ai.respond('load aiml b')  # faz com que os outros arquivos da AIML sejam carregados

print("Obtendo atualização".center(50, '-'))


def process_message(bot, u):  # This is what we'll do when we get a message

    if u.message.sender and u.message.text and u.message.chat:  # if it is a text message then get it
        chat_id = u.message.chat.id
        user = u.message.sender.username
        message = u.message.text
        recebida = message
        resposta_bot = (ai.respond(recebida))
        bot.send_message(chat_id, resposta_bot)
        if message == 'clima':  # if the user is asking for the weather then we ask the location
            bot.send_message(chat_id, 'please send me your location')

    if u.message.location:  # if the message contains a location then get the weather on that latitude/longitude
        print(u.message.location)
        chat_id = u.message.chat.id
        owm = OWM(OWMKEY)  # initialize the Weather API
        obs = owm.weather_at_coords(u.message.location.latitude,
                                    u.message.location.longitude)  # Create a weather observation
        w = obs.get_weather()  # create the object Weather as w
        print(w)  # <Weather - reference time=2013-12-18 09:20, status=Clouds>
        l = obs.get_location()  # create a location related to our already created weather object And send the parameters
        status = str(w.get_detailed_status())
        placename = str(l.get_name())
        wtime = str(w.get_reference_time(timeformat='iso'))
        temperature = str(w.get_temperature('celsius').get('temp'))
        bot.send_message(chat_id,
                         'Weather Status: ' + status + ' Cidade: ' + placename + ' ' + wtime + ' Temperatura: ' + temperature + 'C')  # send the anwser


while True:  # a loop to wait for messages
    updates = bot.get_updates(offset=last_update_id).wait()  # we wait for a message
    try:
        for update in updates:  # get the messages
            if int(update.update_id) > int(last_update_id):  # if it is a new message then get it
                last_update_id = update.update_id
                process_message(bot, update)  # send it to the function
                continue
        continue
    except Exception:
        ex = None
        print(traceback.format_exc())
        continue
