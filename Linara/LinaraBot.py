# -*- coding: utf-8 -*-

from twx.botapi import *
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

    _MessageBase = namedtuple('Message', [
        'message_id', 'sender', 'date', 'edit_date', 'chat', 'forward_from', 'forward_from_chat',
        'forward_from_message_id', 'forward_date',
        'reply_to_message', 'text', 'entities', 'audio', 'document', 'photo', 'sticker',
        'video', 'voice', 'caption', 'contact', 'location', 'venue', 'new_chat_member',
        'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo',
        'group_chat_created', 'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id',
        'migrate_from_chat_id', 'pinned_message'])


    class Message(_MessageBase):

        """This object represents a message.
        Attributes:
            message_id       (int)                           :Unique message identifier
            sender           (User)                          :*Optional.* Sender, can be empty for messages sent to channels
            date             (int)                           :Date the message was sent in Unix time
            chat             (Chat)                          :Conversation the message belongs to
            forward_from     (User)                          :*Optional.* For forwarded messages, sender of the original message
            forward_from_chat (Chat)                         :*Optional.* For messages forwarded from a channel, information about
                                                                          the original channel
            forward_from_message_id (int)                    :*Optional.* For forwarded channel posts, identifier of the original message in the channel
            forward_date     (int)                           :*Optional.* For forwarded messages, date the original message was
                                                                         sent in Unix time
            reply_to_message (Message)                       :*Optional.* For replies, the original message. Note that the
                                                                          Message object in this field will not contain further
                                                                          reply_to_message fields even if it itself is a reply.
            edit_date        (int)                           :*Optional.* Date the message was last edited in Unix time
            text             (str)                           :*Optional.* For text messages, the actual UTF-8 text of the message
            entities         (Sequence[MessageEntity])       :*Optional.*For text messages, special entities like usernames,
                                                                         URLs, bot commands, etc. that appear in the text
            audio            (Audio)                         :*Optional.* Message is an audio file, information about the file
            document         (Document)                      :*Optional.* Message is a general file, information about the file
            game             (Game)                          :*Optional.* Message is a game, information about the game.
            photo            (Sequence[PhotoSize])           :*Optional.* Message is a photo, available sizes of the photo
            sticker          (Sticker)                       :*Optional.* Message is a sticker, information about the sticker
            video            (Video)                         :*Optional.* Message is a video, information about the video
            voice            (Voice)                         :*Optional.* Message is a voice message, information about the file
            caption          (str)                           :*Optional.* Caption for the photo or video
            contact          (Contact)                       :*Optional.* Message is a shared contact, information about
                                                                          the contact
            location         (Location)                     :*Optional.* Message is a shared location, information about the
                                                                         location
            venue           (Venue)                         :*Optional.* Message is a venue, information about the venue
            new_chat_member    (User)                       :*Optional.* A new member was added to the group, information about
                                                                         them (this member may be bot itself)
            left_chat_member   (User)                       :*Optional.* A member was removed from the group, information about
                                                                         them (this member may be bot itself)
            new_chat_title          (str)                   :*Optional.* A group title was changed to this value
            new_chat_photo          (Sequence[PhotoSize])   :*Optional.* A group photo was change to this value
            delete_chat_photo       (bool)                  :*Optional.* Informs that the group photo was deleted
            group_chat_created      (bool)                  :*Optional.* Informs that the group has been created
            supergroup_chat_created (bool)                  :*Optional.* Service message: the supergroup has been created
            channel_chat_created    (bool)                  :*Optional.* Service message: the channel has been created
            migrate_to_chat_id		(int)                   :*Optional.* The group has been migrated to a supergroup with
                                                                         the specified identifier, not exceeding 1e13 by absolute value
            migrate_from_chat_id    (int)                   :*Optional.* The supergroup has been migrated from a group
                                                                         with the specified identifier, not exceeding 1e13 by absolute value
            pinned_message          (Message)               :*Optional.* Specified message was pinned. Note that the Message object in this
                                                                         field will not contain further reply_to_message fields even if it
                                                                         is itself a reply.
        """
        __slots__ = ()

        @property
        def new_chat_participant(self):
            print("DEPRECATED: new_chat_participant is now new_chat_member")
            return self.new_chat_member

        @property
        def left_chat_participant(self):
            print("DEPRECATED: left_chat_participant is now left_chat_member")
            return self.left_chat_member

        @staticmethod
        def from_result(result):
            if result is None:
                return None

            # photo is a list of PhotoSize
            photo = result.get('photo')
            if photo is not None:
                photo = [PhotoSize.from_result(photo_size) for photo_size in photo]

            # entities is a list of MessageEntity
            entities = result.get('entities')
            if entities is not None:
                entities = [MessageEntity.from_result(entity) for entity in entities]

            text = result.get('text')
            if text is not None:
                text = [MessageEntity.from_result(tex) for tex in text]

            return Message(
                message_id=result.get('message_id'),
                sender=User.from_result(result.get('from')),
                date=result.get('date'),
                edit_date=result.get('edit_date'),
                chat=Chat.from_result(result.get('chat')),
                forward_from=User.from_result(result.get('forward_from')),
                forward_from_chat=Chat.from_result(result.get('forward_from_chat')),
                forward_from_message_id=Message.from_result(result.get('forward_from_message_id')),
                forward_date=result.get('forward_date'),
                reply_to_message=Message.from_result(result.get('reply_to_message')),
                text=result.get('text'),
                entities=entities,
                audio=Audio.from_result(result.get('audio')),
                document=Document.from_result(result.get('document')),
                photo=photo,
                sticker=Sticker.from_result(result.get('sticker')),
                video=Video.from_result(result.get('video')),
                voice=Voice.from_result(result.get('voice')),
                caption=result.get('caption'),
                contact=Contact.from_result(result.get('contact')),
                location=Location.from_result(result.get('location')),
                venue=Venue.from_result(result.get('venue')),
                new_chat_member=User.from_result(result.get('new_chat_member')),
                left_chat_member=User.from_result(result.get('left_chat_member')),
                new_chat_title=result.get('new_chat_title'),
                new_chat_photo=result.get('new_chat_photo'),
                delete_chat_photo=result.get('delete_chat_photo'),
                group_chat_created=result.get('group_chat_created'),
                supergroup_chat_created=result.get('supergroup_chat_created'),
                channel_chat_created=result.get('channel_chat_created'),
                migrate_to_chat_id=result.get('migrate_to_chat_id'),
                migrate_from_chat_id=result.get('migrate_from_chat_id'),
                pinned_message=Message.from_result(result.get('pinned_message'))
            )
        print('TEXTO', Message.text)
        sleep(2)