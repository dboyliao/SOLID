#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class IEmail(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def setSender(self, sender):
        pass

    @abstractmethod
    def setReceiver(self, receiver):
        pass

    @abstractmethod
    def setContent(self, content):
        pass

class Email(IEmail):

    def __init__(self, protocol, content_type):
        self.protocol = protocol
        self.content_type = content_type
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def setSender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def setReceiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def setContent(self, content):
        if self.content_type == 'MyML':
            self.__content = '\n'.join(['<myML>', content, '</myML>'])
        else:
            self.__content = content

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)

def main():
    email = Email('IM', 'MyML')
    email.setSender('qmal')
    email.setReceiver('james')
    email.setContent('Hello, there!')
    print email

if __name__ == '__main__':
    main()
