#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Skullbot - A simple TwitchBot"""

import socket
import json
import time
import random
import re
from settings import channel, server, oauth_password, nickname


class IRC(object):
    'defines IRC connection object'
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        'sends message to irc'
        self.irc.send("PRIVMSG %s :%s\n" % (chan, msg.encode('utf-8')))

    def connect(self, server, channel, botnick, oauth_password):
        'defines the socket'
        print "Connecting to:" + server
        self.irc.connect((server, 6667))
        self.irc.send("USER %s\r\n" % botnick)
        self.irc.send("PASS %s\r\n" % oauth_password)
        self.irc.send("NICK %s\r\n" % botnick)
        self.irc.send("JOIN %s\r\n" % channel)

    def get_text(self):
        'receive the text'
        text = self.irc.recv(2040)

        if text.find('PING') != -1:
            self.irc.send('PONG %s\r\n' % text.split()[1])

        return text


def main():
    '''Checks incoming irc messages for trigger phrases,
    returns messages in response'''

    irc = IRC()
    irc.connect(server, channel, nickname, oauth_password)


    while True:
        chat_message = irc.get_text()
        print chat_message

        if "PRIVMSG" in chat_message and channel in chat_message:
            with open("responses.json", "r") as f:
                responses = json.loads(f.read())
                for k in responses:
                    if re.search(k, chat_message.lower()):
                        if isinstance(responses.get(k), dict):
                            alias_key = responses.get(k).get("alias")
                            message = responses.get(alias_key)
                            if isinstance(message, list):
                                message = random.choice(message)
                        elif isinstance(responses.get(k), list):
                            message = random.choice(responses.get(k))
                        else:
                            message = responses.get(k)
                        irc.send(channel, message)
                        time.sleep(5)
                        break

if __name__ == "__main__":
    main()
