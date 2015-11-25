#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import time

class AbstractWorker(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Worker(AbstractWorker):

    def work(self):
        print "I'm normal worker. I'm working."

    def eat(self):
        print "Lunch break....(5 secs)"
        time.sleep(5)

class SuperWorker(AbstractWorker):

    def work(self):
        print "I'm super worker. I work very hard!"

    def eat(self):
        print "Lunch break....(3 secs)"
        time.sleep(3)


class Manager(object):

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorker), "`worker` must be of type {}".format(AbstractWorker)

        self.worker = worker

    def manage(self):
        self.worker.work()

    def lunch_break(self):
        self.worker.eat()

# Implement the `Robot` class. However, due to the api defined by `AbstractWorker`,
# we have to reimplement `eat` method which is not necessary for a `Robot`.

class Robot(AbstractWorker):

    def work(self):
        print "I'm a robot. I'm working...."

    def eat(self):
        print "I don't need to eat...."   # This code doing nothing but it is a must. (Bad!)

def main():

    manager = Manager()
    manager.set_worker(Worker())
    # Make normal worker works.
    manager.manage()
    # lunch break
    manager.lunch_break()

    # super worker
    manager.set_worker(SuperWorker())
    manager.manage()
    manager.lunch_break()

    manager.set_worker(Robot())
    manager.manage()
    # However, a robot can eat.....
    manager.lunch_break()

if __name__ == '__main__':
    main()
