import os
import aiml

class Connect(object):

    def AIML_START(self):
        os.chdir('C:/Users/Roberto Maier/PycharmProjects/LinaraBot/LinaraBot_AIML/botdata/standard') # diretório que contém os arquivos da AIML standard
        ai = aiml.Kernel()# inicialização
        ai.learn('startup.xml')  # lê o arquivo principal da AIML e faz referências aos outros
        ai.respond('load aiml b')  # faz com que os outros arquivos da AIML sejam carregados
        while (1 == 1):
            frase = input('Fale algo ao bot em english:')
            return print ("Resposta do bot: %s" % ai.respond(frase))