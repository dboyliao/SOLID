#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Here we solve the issues in the design in `python_code.bad.DIP` with an interface
# (implemented with abstract class).

from abc import ABCMeta, abstractmethod

class IWorker(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def work(self):
        pass

# `IWorker` defines a interface which requires `work` method.

class Worker(IWorker):

    def work(self):
        print("I'm working!!")


class Manager(object):

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, IWorker), '`worker` must be of type {}'.format(Worker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()
            # And some complex codes go here....

class SuperWorker(IWorker):

    def work(self):
        print("I work very hard!!!")

# Now, the manager support `SuperWorker`...
# In addition, it will support any worker which obeys the interface defined by `IWorker`!

def main():

    worker = Worker()
    manager = Manager()
    manager.set_worker(worker)
    manager.manage()

    # The following will work!
    super_worker = SuperWorker()
    try:
        manager.set_worker(super_worker)
        manager.manage()
    except AssertionError:
        print("manager fails to support super_worker....")

if __name__ == "__main__":
    main()
