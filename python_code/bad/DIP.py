#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Worker(object):

    def work(self):
        print("I'm working!!")


class Manager(object):

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Worker), '`worker` must be of type {}'.format(Worker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()
            # And some complex codes go here....

class SuperWorker(object):

    def work(self):
        print("I work very hard!!!")

# OK... now you can see what happend if we want the `Manager` to support `SuperWorker`.
#  1. The `set_worker` must be modified or it will not pass the type-checking.
#  2. The `manage` method should be re-test, which means you may or may not have to 
#     rewrite the testing code.

def main():

    worker = Worker()
    manager = Manager()
    manager.set_worker(worker)
    manager.manage()

    # The following will not work...
    super_worker = SuperWorker()
    try:
        manager.set_worker(super_worker)
    except AssertionError:
        print("manager fails to support super_worker....")

if __name__ == "__main__":
    main()
